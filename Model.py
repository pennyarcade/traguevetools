import peewee
import local_settings

db = peewee.MySQLDatabase(
    local_settings.MySqlName,
    host=local_settings.MySqlHost,
    user=local_settings.MySqlUser,
    passwd=local_settings.MySqlPwd
)

class InvType(peewee.Model):
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
    typeId = peewee.PrimaryKeyField(db_column='typeId')
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

def get_model_from_dictionary(model, field_dict):
    if isinstance(model, Model):
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
        if isinstance(field_obj, pewee.ForeignKeyField) and field_data and field_obj.rel_model in fields:
            rel_obj = getattr(model, field_name)
            data[field_name] = get_dictionary_from_model(rel_obj, fields, exclude)
        else:
            data[field_name] = field_data
    return data
