from sql_alchemy import banco

class AccountModel(banco.Model):
    __tablename__ = 'account'
    account_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(40), nullable=False)
    initial_balance = banco.Column(banco.Float, default=0)
    credits = banco.relationship('CreditModel')
    debits = banco.relationship('DebitModel')
    
    def __init__(self, name, initial_balance):
        self.name = name
        self.initial_balance = initial_balance

    def json(self):
        return {
            "account_number": self.account_id,
            "name": self.name,
            "initial_balance": self.initial_balance,
        }


    @classmethod
    def find(cls, account_id):
        return cls.query.filter_by(account_id=account_id).first()

    @classmethod
    def find_all(cls, limit=50, offset=0):
        return cls.query.limit(limit).offset(offset).all()

    def save(self):
        banco.session.add(self)
        banco.session.commit()