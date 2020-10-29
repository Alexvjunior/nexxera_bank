from flask_restful import Resource, reqparse
from models.account import AccountModel
from utility import errors, server_code
import traceback

_ARGUMENTS = reqparse.RequestParser()
_ARGUMENTS.add_argument('name', type=str, required=True, help="This field canot be null")
_ARGUMENTS.add_argument('initial_balance', type=float)
_ARGUMENTS_FILTER = reqparse.RequestParser()
_ARGUMENTS_FILTER.add_argument('account_id', type=int)
_ARGUMENTS_FILTER.add_argument('limit', type=float)
_ARGUMENTS_FILTER.add_argument('offset', type=float)


class Accounts(Resource):
    def get(self):
        data = _ARGUMENTS_FILTER.parse_args()
        accounts = AccountModel.find_all(limit=data.get('limit'), offset=data.get('offset'))
        return {"accounts": [account.json() for account in accounts]}

class Account(Resource):
    def get(self):
        data = _ARGUMENTS_FILTER.parse_args()
        account = AccountModel.find(data.get('account_id'))
        if account is None:
            return errors._NOT_FOUND
        return account.json(), server_code.OK
    
class AccountRegister(Resource):
    def post(self):
        argument_data = _ARGUMENTS.parse_args()
        user = AccountModel(**argument_data)
        try:
            user.save()
        except Exception as e:
            traceback.print_exc()
            return errors._SAVE_ERROR, server_code.INTERNAL_SERVER_ERROR
        return user.json(), server_code.OK