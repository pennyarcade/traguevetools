from flask import Blueprint
from flask import render_template

from flask_login import current_user

from evetools.api.esi import esisecurity, esiclient, esiapp

index = Blueprint('index', __name__, template_folder='templates')


# -----------------------------------------------------------------------
# Index Routes
# -----------------------------------------------------------------------
@index.route('/')
def indexfunc():
    wallet = None

    # if the user is authed, get the wallet content !
    if current_user.is_authenticated:
        # give the token data to esisecurity, it will check alone
        # if the access token need some update
        esisecurity.update_token(current_user.get_sso_data())

        op = esiapp.op['get_characters_character_id_wallets'](
            character_id=current_user.character_id
        )
        wallet = esiclient.request(op)

    return render_template('base.html', **{
        'wallet': wallet,
    })
