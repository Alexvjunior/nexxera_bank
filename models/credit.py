from sql_alchemy import banco


class CreditModel(banco.Model):
    __tablename__ = 'credit'

    credit_id = banco.Column(banco.Integer, primary_key=True)
    value = banco.Column(banco.Float, nullable=False)
    description = banco.Column(banco.String, nullable=False)
    account_id = banco.Column(
        banco.Integer, banco.ForeignKey('account.account_id'))

    def __init__(self, account_id, value, description):
        self.account_id = account_id
        self.value = value
        self.description = description

    def json(self):
        return {
            "credit_id": self.credit_id,
            "account_number": self.account_id,
            "value": self.value,
            "description": self.description,
        }

    @classmethod
    def find_credits(cls, account_id, limit=50, offset=0):
        return cls.query.filter_by(account_id=account_id).limit(limit).offset(offset)

    @classmethod
    def find_all_credits(cls, account_id):
        return cls.query.filter_by(account_id=account_id)
        
    def save(self):
        banco.session.add(self)
        banco.session.commit()
