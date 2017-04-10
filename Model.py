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
    typeId = peewee.IntegerField(db_column='typeId', index=True)
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

    class Meta:
        database = db
        db_table = 'invTypes'