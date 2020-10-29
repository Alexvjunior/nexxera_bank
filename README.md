# Nexxera Bank

Welcome to the Nexxera Bank, this api will show you all the benefits of a RESTFUL API. Are you ready?

## Installation

Use the latest version of [python](https://www.python.org/downloads/) on your machine, be it linux, windowns or Mac.

You must also have the [docker](https://www.docker.com/) installed on your machine

Right after installing python, you will need to install [pytest](https://docs.pytest.org/en/stable/)
```bash
pip install pytest
```

## Usage

Are we going to start using our API?

1º- First, we must create the image of our API docker.
```bash
docker build -t app .
```
2º- Second, we must upload our container with this image that we have just created
```bash
docker run -d -p 5000:5000 --name app_container app
```
Awesome, know our API is running. A tip, if you already have the `make` tool installed on your machine, just run the following command:
```bash
make check
```
Very easy isn't it?

Now we can perform all of our requests for our API. Here is the list of the features that we have in our API:
```text
http://localhost:5000/account/register - POST
http://localhost:5000/account - GET
http://localhost:5000/accounts - GET
```
These urls are for our account creation and viewing. To register an account, we must pass the body as follows:
```json
{
"name":"person_name",
"initial_balance":30
}
```
In this case our `name` field is mandatory. To view a specific account, we must use the path `http://localhost:5000/account` and we have 3 types of filters passing as parameters:
```text
account_id
limit
offset
```

Our next paths are:
```text
http://localhost:5000/debit/register
http://localhost:5000/debits
```
These urls are for our debits creation and viewing. To register an debit, we must pass the body as follows:
```json
{
"value": 300,
"account_id": 2,
"description" : "description"
}
```
In this way, all fields are mandatory. To search for all debits in an account, we must pass the `account_id` field in the filter and use the path `http://localhost:5000/debits`

Our next paths are:
```text
http://localhost:5000/credit/register
http://localhost:5000/credits
```
These urls are for our creditscreation and viewing. To register an credit, we must pass the body as follows:
```json
{
"value": 300,
"account_id": 2,
"description" : "description"
}
```
In this way, all fields are mandatory. To search for all creditsin an account, we must pass the `account_id` field in the filter and use the path `http://localhost:5000/credits`


Our last path would be to visualize the extract, we only have visualization in that path, but with the following filters:
```text
account_id
limit
offset
credit_debit
```
Our `account_id` filter is mandatory, but our other fields are not. To perform the search for credits only, just use the `credit_debit` filter to set it to 0 and to search only debits, just pass 1, if you want to bring everything, just don't pass the filter as parameter.

## Tests
Our best time has come, testing. For you who have the `make` command installed on your machine, just perform the `make test_coverage` command on your terminal, with this our API will show our tests. If you do not have the make command, do not be alarmed, in our installation we perform the installation of a python library, the pytest, to run it just at the end run the following command:
```bash
python -m pytest .\test\test_resources.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.