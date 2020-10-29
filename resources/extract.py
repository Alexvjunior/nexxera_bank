from flask_restful import Resource, reqparse
from models.account import AccountModel
from models.debit import DebitModel
from models.credit import CreditModel
from utility import errors, server_code

_ARGUMENTS = reqparse.RequestParser()
_ARGUMENTS.add_argument('account_id', type=int)
_ARGUMENTS.add_argument('credit_debit', type=int)


class Extract(Resource):

    def get(self):
        params = _ARGUMENTS.parse_args()
        account_id = params.get('account_id')
        credit_debit = params.get('credit_debit')
        user = AccountModel.find(account_id)
        credits = []
        debits = []
        if user is None:
            return errors._USER_NOT_FOUND, server_code.NOT_FOUND
        if credit_debit is None:
            credits = CreditModel.find_all_credits(account_id)
            debits = DebitModel.find_all_credits(account_id)
        elif credit_debit == 0:
            credits = CreditModel.find_all_credits(account_id)
        elif credit_debit == 1:
            debits = DebitModel.find_all_credits(account_id)

        result = user.json()
        result["debits"] = [debit.json() for debit in debits]
        result["credits"] = [credit.json() for credit in credits]
        result["amount_credits"] = amount_credits = self.__sum(credits)
        result["amount_debits"] = amount_debits = self.__sum(debits)
        result["amount"] = user.initial_balance + amount_credits - amount_debits
        return result, server_code.OK

    def __sum(self, credits_debits):
        if credits_debits is None:
            return 0
        result_sum = 0
        [result_sum := result_sum + credit_debit.value for credit_debit in credits_debits]
        return result_sum
