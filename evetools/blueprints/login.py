from flask import Blueprint
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from esipy.exceptions import APIException
from sqlalchemy.orm.exc import NoResultFound

from evetools import db, logger
from evetools.api.esi import esisecurity
from evetools.model.user import User


login = Blueprint('login', __name__, template_folder='templates')


# -----------------------------------------------------------------------
# Login / Logout Routes
# -----------------------------------------------------------------------
@login.route('/login')
def login():
    """ this redirects the user to the EVE SSO login """
    return redirect(esisecurity.get_auth_uri(
        scopes=['esi-wallet.read_character_wallet.v1']
    ))


@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@login.route('/sso/callback')
@login.route('/sso/callback/')
def callback():
    """ This is where the user comes after he logged in SSO """
    # get the code from the login process
    code = request.args.get('code')

    # now we try to get tokens
    try:
        auth_response = esisecurity.auth(code)
    except APIException as e:
        return 'Login EVE Online SSO failed: %s' % e, 403

    # we get the character informations
    cdata = esisecurity.verify()

    # if the user is already authed, we log him out
    if current_user.is_authenticated:
        logout_user()

    # now we check in database, if the user exists
    # actually we'd have to also check with character_owner_hash, to be
    # sure the owner is still the same, but that's an example only...
    try:
        user = User.query.filter(
            User.character_id == cdata['CharacterID'],
        ).one()

    except NoResultFound:
        user = User()
        user.character_id = cdata['CharacterID']

    user.character_owner_hash = cdata['CharacterOwnerHash']
    user.character_name = cdata['CharacterName']
    user.update_token(auth_response)

    # now the user is ready, so update/create it and log the user
    try:
        db.session.merge(user)
        db.session.commit()

        login_user(user)
        session.permanent = True

    except:
        logger.exception("Cannot login the user - uid: %d" % user.character_id)
        db.session.rollback()
        logout_user()

    return redirect(url_for("index"))
