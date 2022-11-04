import json
## serializing to json file
accounts_dict = {'accounts': [
                {'account2': 100, 'name': 'Jones', 'balance': 24.98},
                {'account2': 200, 'name': 'Doe', 'balance': 345.67}]}


with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)




