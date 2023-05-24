def repeated_number(st):
  count = 0
  for i in range(len(st)):
    if(st[i] == st[i+1]):
      count += 1
    else:
      count = 0
    if count >= 4:
      return False
    else:
      return True


def sperated(st):
  count = 0
  for i in range(4,16,5):
    if(st[i] == '-'):
      count += 1
  if count == 3:
    return True
  else:
    return False


inputs = ['4253625879615786', '4424424424442444', '5122-2368-7954-3214', '42536258796157867', '442444442442444', '5122-2368-7954 - 3214', '44244x442444244', '0525362587961578']
outputs = []
for credit in inputs:
    if (credit[0] in ['4', '5','6']) and (len(credit) == 16) and (credit.isdigit()) and (credit not in [' ','_']) and (repeated_number(credit)) or (sperated(credit)):
        outputs.append(True)
    else:
        outputs.append(False)

print(outputs)
