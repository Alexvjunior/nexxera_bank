import requests


def test_verify_initinal_accounts():
    r = requests.get('http://localhost:5000/accounts')
    accounts = r.json().get('accounts')
    assert accounts[0] == {'account_number': 1,
                           'initial_balance': 0.0, 'name': 'Fernanda'}
    assert accounts[1] == {'account_number': 2,
                           'initial_balance': 300.0, 'name': 'Alex'}
    assert accounts[2] == {
        "account_number": 3,
        "name": "julia",
        "initial_balance": 50.0
    }


def test_verify_create_account():
    r = requests.post('http://localhost:5000/account/register',
                      data={'name': "TESTE"})
    assert r.status_code == 200


def test_verify_error_create_account():
    r = requests.post('http://localhost:5000/account/register')
    assert r.status_code == 400
    assert r.json() == {"message": {'name': 'This field canot be null'}}


def test_verify_create_debit():
    r = requests.post('http://localhost:5000/debit/register',
                      data={'value': 30, "account_id": 1, "description": "teste"})
    assert r.status_code == 200


def test_verify_error_create_debit():
    r = requests.post('http://localhost:5000/debit/register')
    assert r.status_code == 400
    assert r.json() == {"message": {'value': 'This field canot be null'}}


def test_verify_error_create_debit_only_value():
    r = requests.post('http://localhost:5000/debit/register',
                      data={'value': 30})
    assert r.status_code == 400
    assert r.json() == {"message": {'account_id': 'This field canot be null'}}


def test_verify_error_create_debit_with_value_account():
    r = requests.post('http://localhost:5000/debit/register',
                      data={'value': 30, "account_id": 1})
    assert r.status_code == 400
    assert r.json() == {"message": {'description': 'This field canot be null'}}

def test_verify_create_credit():
    r = requests.post('http://localhost:5000/credit/register',
                      data={'value': 30, "account_id": 1, "description": "teste"})
    assert r.status_code == 200


def test_verify_error_create_credit():
    r = requests.post('http://localhost:5000/credit/register')
    assert r.status_code == 400
    assert r.json() == {"message": {'value': 'This field canot be null'}}


def test_verify_error_create_credit_only_value():
    r = requests.post('http://localhost:5000/credit/register',
                      data={'value': 30})
    assert r.status_code == 400
    assert r.json() == {"message": {'account_id': 'This field canot be null'}}


def test_verify_error_create_credit_with_value_account():
    r = requests.post('http://localhost:5000/credit/register',
                      data={'value': 30, "account_id": 1})
    assert r.status_code == 400
    assert r.json() == {"message": {'description': 'This field canot be null'}}
