import peewee
import local_settings


if local_settings.environment == "prod":
    db = peewee.MySQLDatabase(
        local_settings.MySqlName,
        host=local_settings.MySqlHost,
        user=local_settings.MySqlUser,
        passwd=local_settings.MySqlPwd
    )
else:
    db = peewee.SqliteDatabase('sdc/sqlite-latest.sqlite')


class BaseModel(peewee.Model):
    def toDict(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        return str(r)


class InvType(BaseModel):
    """
        +---------------+---------------+------+-----+---------+-------+
        | Field         | Type          | Null | Key | Default | Extra |
        +---------------+---------------+------+-----+---------+-------+
        | typeID        | int(11)       | NO   | PRI | NULL    |       |
        | groupID       | int(11)       | YES  | MUL | NULL    |       |
        | typeName      | varchar(100)  | YES  |     | NULL    |       |
        | description   | text          | YES  |     | NULL    |       |
        | mass          | double        | YES  |     | NULL    |       |
        | volume        | double        | YES  |     | NULL    |       |
        | capacity      | double        | YES  |     | NULL    |       |
        | portionSize   | int(11)       | YES  |     | NULL    |       |
        | raceID        | int(11)       | YES  |     | NULL    |       |
        | basePrice     | decimal(19,4) | YES  |     | NULL    |       |
        | published     | tinyint(1)    | YES  |     | NULL    |       |
        | marketGroupID | int(11)       | YES  |     | NULL    |       |
        | iconID        | int(11)       | YES  |     | NULL    |       |
        | soundID       | int(11)       | YES  |     | NULL    |       |
        | graphicID     | int(11)       | YES  |     | NULL    |       |
        +---------------+---------------+------+-----+---------+-------+
    """
    typeID = peewee.PrimaryKeyField(db_column='typeId')
    groupID = peewee.IntegerField(db_column='groupID')
    typeName = peewee.CharField(max_length=100, db_column='typeName')
    description = peewee.TextField(db_column='description')
    mass = peewee.DoubleField(db_column='mass')
    volume = peewee.DoubleField(db_column='volume')
    capacity = peewee.DoubleField(db_column='capacity')
    portionSize = peewee.IntegerField(db_column='portionSize')
    raceID = peewee.IntegerField(db_column='raceID')
    basePrice = peewee.DecimalField(max_digits=19, decimal_places=4, db_column='basePrice')
    published = peewee.BooleanField(db_column='published')
    marketGroupID = peewee.IntegerField(db_column='marketGroupID')
    iconID = peewee.IntegerField(db_column='iconID')
    soundID = peewee.IntegerField(db_column='soundID')
    graphicID = peewee.IntegerField(db_column='graphicID')
    sorted_field_names = [
        'typeId', 'groupID', 'typeName', 'description', 'mass', 'volume',
        'capacity', 'portionSize', 'raceID', 'basePrice', 'published',
        'marketGroupID', 'iconID', 'soundID', 'graphicID'
    ]

    class Meta:
        database = db
        db_table = 'invTypes'


class WalletTransactions(BaseModel):
    """
        +------------------+---------------+------+-----+---------+-------+
        | Field            | Type          | Null | Key | Default | Extra |
        +------------------+---------------+------+-----+---------+-------+
        | amount           | decimal(19,2) | YES  |     | NULL    |       |
        | argumentName     | varchar(255)  | YES  |     | NULL    |       |
        | argumentValue    | int(11)       | YES  |     | NULL    |       |
        | balance          | decimal(19,2) | YES  |     | NULL    |       |
        | date             | date          | YES  |     | NULL    |       |
        | firstPartyID     | int(11)       | YES  |     | NULL    |       |
        | firstPartyType   | varchar(20)   | YES  |     | NULL    |       |
        | reason           | text          | YES  |     | NULL    |       |
        | refID            | int(11)       | NO   | PRI | NULL    |       |
        | refTypeID        | int(11)       | YES  | MUL | NULL    |       |
        | secondPartyID    | int(11)       | YES  |     | NULL    |       |
        | secondPartyType  | varchar(20)   | YES  |     | NULL    |       |
        | taxAmount        | decimal(19,2) | YES  |     | NULL    |       |
        | taxRecieverID    | int(11)       | YES  |     | NULL    |       |
        +------------------+---------------+------+-----+---------+-------+
    """
    amount = peewee.DecimalField(max_digits=19, decimal_places=4, db_column='amount', null=True)
    argumentName = peewee.CharField(max_length=255, db_column='argument_name', null=True)
    argumentValue = peewee.IntegerField(db_column='argument_value', null=True)
    balance = peewee.DecimalField(max_digits=19, decimal_places=4, db_column='balance', null=True)
    date = peewee.DateTimeField(db_column='date')
    firstPartyID = peewee.IntegerField(db_column='first_party_id', null=True)
    firstPartyType = peewee.CharField(max_length=20, db_column='first_party_type', null=True)
    reason = peewee.TextField(db_column='reason', null=True)
    refID = peewee.PrimaryKeyField(db_column='refId')
    refTypeID = peewee.IntegerField(db_column='refTypeId')
    secondPartyID = peewee.IntegerField(db_column='second_party_id', null=True)
    secondPartyType = peewee.CharField(max_length=20, db_column='second_party_type', null=True)
    taxAmount = peewee.DecimalField(max_digits=19, decimal_places=4, db_column='taxAmount', null=True)
    taxRecieverID = peewee.IntegerField(db_column='tax_reciever_id', null=True)

    sorted_field_names = [
        'refID', 'refTypeID', 'amount', 'balance', 'reason', 'date',
        'argumentName', 'argumentValue', 'firstPartyID', 'firstPartyType',
        'secondPartyID', 'secondPartyType', 'taxAmount', 'taxRecieverID'
    ]

    class Meta:
        database = db
        db_table = 'walletTransactions'


class EsiUser(BaseModel):
    """

    """
    charID = peewee.PrimaryKeyField(db_column='character_id')
    charOwnerHash = peewee.CharField(max_length=255, db_column='char_owner_hash')
    charName = peewee.CharField(max_length=200, db_column='char_name')
    accessToken = peewee.CharField(max_length=100, db_column='access_token')
    accessTokenExpires = peewee.DateTimeField(db_column='access_token_expired')
    refreshToken = peewee.CharField(max_length=100, db_column='refresh_token')
    sorted_field_names = [
        'charID', 'charOwnerHash', 'charName',
        'accessToken', 'accessTokenExpires', 'refreshToken'
    ]

    def get_id(self):
        """ Required for flask-login """
        return self.character_id

    def get_sso_data(self):
        """ Little "helper" function to get formated data for esipy security
        """
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires_in': (
                self.access_token_expires - datetime.utcnow()
            ).total_seconds()
        }

    def update_token(self, token_response):
        """ helper function to update token data from SSO response """
        self.access_token = token_response['access_token']
        self.access_token_expires = datetime.fromtimestamp(
            time.time() + token_response['expires_in'],
        )
        if 'refresh_token' in token_response:
            self.refresh_token = token_response['refresh_token']

    class Meta:
        database = db
        db_table = 'esiUser'


def get_model_from_dictionary(model, field_dict):
    if isinstance(model, peewee.Model):
        model_instance = model
        check_fks = True
    else:
        model_instance = model()
        check_fks = False
    models = [model_instance]
    for field_name, value in field_dict.items():
        field_obj = model._meta.fields[field_name]
        if isinstance(value, dict):
            rel_obj = field_obj.rel_model
            if check_fks:
                try:
                    rel_obj = getattr(model, field_name)
                except field_obj.rel_model.DoesNotExist:
                    pass
                if rel_obj is None:
                    rel_obj = field_obj.rel_model
            rel_inst, rel_models = get_model_from_dictionary(rel_obj, value)
            models.extend(rel_models)
            setattr(model_instance, field_name, rel_inst)
        else:
            setattr(model_instance, field_name, field_obj.python_value(value))
    return model_instance, models


def get_dictionary_from_model(model, fields=None, exclude=None):
    model_class = type(model)
    data = {}

    fields = fields or {}
    exclude = exclude or {}
    curr_exclude = exclude.get(model_class, [])
    curr_fields = fields.get(model_class, model.sorted_field_names)

    for field_name in curr_fields:
        if field_name in curr_exclude:
            continue
        field_obj = model_class._meta.fields[field_name]
        field_data = model._data.get(field_name)
        if isinstance(field_obj, peewee.ForeignKeyField) and field_data and field_obj.rel_model in fields:
            rel_obj = getattr(model, field_name)
            data[field_name] = get_dictionary_from_model(rel_obj, fields, exclude)
        else:
            data[field_name] = field_data
    return data
