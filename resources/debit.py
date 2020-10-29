from flask_restful import Resource, reqparse
from models.debit import DebitModel
from models.account import AccountModel
from utility import errors, server_code
import traceback

_ARGUMENTS = reqparse.RequestParser()
_ARGUMENTS.add_argument('value', type=float, required=True, help="This field canot be null")
_ARGUMENTS.add_argument('account_id', type=int, required=True, help="This field canot be null")
_ARGUMENTS.add_argument('description', type=str, required=True, help="This field canot be null")
_ARGUMENTS_FILTER = reqparse.RequestParser()
_ARGUMENTS_FILTER.add_argument('account_id', type=int)
_ARGUMENTS_FILTER.add_argument('limit', type=float)
_ARGUMENTS_FILTER.add_argument('offset', type=float)

class Debits(Resource):
    path_params = reqparse.RequestParser()
    path_params.add_argument('account_id', type=int)

    def get(self):
        params = _ARGUMENTS_FILTER.parse_args()
        debits = DebitModel.find_debits(params.get('account_id'), params.get('limit'), params.get('offset'))
        if debits is None:
            return errors._NOT_FOUND
        return {"debits": [debit.json() for debit in debits]}, server_code.OK

class DebitRegister(Resource):
    def post(self):
        arguments_data = _ARGUMENTS.parse_args()
        error, code = self.__validate_value(arguments_data)
        if error is not None:
            return error, code
        debit = DebitModel(**arguments_data)
        try:
            debit.save()
        except Exception as e:
            traceback.print_exc()
            return errors._SAVE_ERROR, server_code.INTERNAL_SERVER_ERROR
        return debit.json(), server_code.OK
    
    def __validate_value(self, arguments_data):
        if arguments_data is None:
            return errors._NOT_FOUND, server_code.INTERNAL_SERVER_ERROR
        if AccountModel.find(arguments_data.get('account_id')) is None:
            return errors._USER_NOT_FOUND, server_code.BAD_REQUEST
        if arguments_data.get("value") <= 0:
            return errors._VALUE_ERROR, server_code.BAD_REQUEST
        return None, None