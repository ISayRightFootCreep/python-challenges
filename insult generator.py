import random
insults = ["'s mom is so stupid, she thought a fax machine had facts", "'s mom is so fat, her splash attack does damage", "'s mom is so ugly, it made gollum look like a model"]
number = random.randint(0, 2)


while True:
    try:
        name = str(input("input a persons name: "))
        break
    except:
        print('you donkey that isnt a name')
print(name, insults[number])
