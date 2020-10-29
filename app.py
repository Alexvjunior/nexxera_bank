from flask import Flask
from flask_restful import Api
from utility import server_code
from resources.extract import Extract
from resources.credit import Credits, CreditRegister
from resources.debit import Debits, DebitRegister
from resources.account import Account, Accounts, AccountRegister

_APP = Flask(__name__)
_APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
_APP.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
_API = Api(_APP)

@_APP.before_first_request
def create_data_base():
    banco.create_all()

_API.add_resource(Extract, '/extract')
_API.add_resource(Account, '/account')
_API.add_resource(Accounts, '/accounts')
_API.add_resource(AccountRegister, '/account/register')
_API.add_resource(Debits, '/debits')
_API.add_resource(DebitRegister, '/debit/register')
_API.add_resource(Credits, '/credits')
_API.add_resource(CreditRegister, '/credit/register')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(_APP)
    _APP.run(host="0.0.0.0", port=5000, debug=True)
