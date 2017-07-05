import sys
sys.path.append("..")

# Imports
import logging
from model import Model

logging.basicConfig(
    filename='logs/scripts.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logging.info('Connecting to model...')
print('Connecting to model...')
Model.db.connect()
logging.info('Connected, creating tables...')
print('Connected, creating tables...')
Model.db.create_tables(
    [
        Model.InvType,
        Model.WalletTransactions
    ],
    safe=True
)
logging.info('Done...')
print('Done...')
