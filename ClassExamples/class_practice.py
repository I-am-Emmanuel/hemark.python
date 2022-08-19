"""holiday = ["month", "January", "february", "march"]
print(holiday)
holiday.reverse()
print(holiday)"""


# bruce force approach
def double_sum(arr: list, target: int) -> list:
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


print(double_sum([3, 7, 8, 12, 17, 1], 11))


# balance_sphere
def balance_pair(brackets: str) -> bool:
    # if brackets.strip() == "" or len(brackets) % 2 == 1:
    if not brackets or len(brackets) % 2 == 1:
        return False

    stack: list = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "}])":

            peek = stack[-1]

            if peek == "{" and bracket == "}":
                stack.pop()
            elif peek == "[" and bracket == "]":
                stack.pop()
            elif peek == "(" and bracket == ")":
                stack.pop()
            else:
                return False
            # pass
            # ... (eclipse can also be used in place of pass)
        else:
            return False

    return True


print(balance_pair("({}"))


#tuple
love = (9, 12, 13, [14, 15, 18], [20, "story", "again", "adamonlekun", 99], 0.12)
print(love)
love[-2][-1] = "Akanji"
print(love)

#dictionary
Girls = dict(a="Abidemi", b="Boluwatife", c="Christiana",
             d="Dolapo", e="Esther")
print(Girls.get("c"))
print(Girls.pop("a"))
print(Girls)

account_name = dict(Name="Adesola Isreal", Gender= "Male", Address= "No 12, Akinpelu street, Sango",
                     Age= 29)
print(account_name)
print(account_name.get("Name"))
print(account_name.update(Name="Ogunsola Williams"))
print(account_name)
for key in account_name:
    print(key)
for key in account_name.items():
    print(key)
for key, value in account_name.items():
    print(f"{key} --> {value}")
