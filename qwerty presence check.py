text = str(input('type some text here'))
qwerty = False
for i in range(len(text)):
    if text[i] == 'q' or text[i] == 'w' or text[i] == 'e' or text[i] == 't' or text[i] == 'y':
        qwerty = True
        break
if qwerty == True:
    print('your text does have qwerty characters')
else:
    print('your text doesnt have qwerty characters')
