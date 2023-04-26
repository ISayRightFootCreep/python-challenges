multiples = []
while True:
  try:
    limit1 = int(input('gib numbr for amt of multiple tables'))
    limit2 = int(input('giv numbr for limit on amt of multiples'))
    break
  except:
    print('stupid that not a valid number')
for i in range(limit1):
  for j in range(limit2):
    multiple = (j + 1) * (i + 1)
    multiples.append(multiple)
  print(multiples)
  multiples = []
