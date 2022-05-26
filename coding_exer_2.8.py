groceries = {"chicken": 8, "apples": 6, "cucucmbers": 3, "milk": 2, "oranges": 4}

remove = groceries.pop("oranges")

print(groceries)

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
name = speakers.keys()
print(name)

tryouts = {"Carl": "passed", "Quentin": "failed", "John Y.": "passed", "Peter": "failed", "Max T.": "passed", "Joseph": "passed", "Jone": "failed", "Jorge": "failed", "George": "passed", "Ben": "passed", "Jerome": "passed", "Rick": "failed", "Max G.": "failed", "John P.": "failed", "Vince": "passed"}
best_friend = tryouts.get("Jorge")

print(best_friend)