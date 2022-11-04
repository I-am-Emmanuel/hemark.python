import json

# deserializing to original python file
with open('accounts.json', 'r') as accounts:
    json_accounts = json.load(accounts)

print(json_accounts)
print(json_accounts['accounts'])
# print(json_accounts['accounts'][0])


# with open('accounts.json', 'r') as accounts:
#     print(json.dumps(json.load(accounts), indent=3))

