import sys
sys.path.append("..")

# Imports
import logging
from model import Model

print('Connecting to model...')
Model.db.connect()
print('Connected, creating tables...')
Model.db.create_table(Model.InvType, safe=True)
Model.db.create_table(Model.WalletTransactions, safe=True)

print('Done...')
