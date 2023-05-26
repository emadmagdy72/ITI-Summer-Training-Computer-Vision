# lst=[20,30,45,10,60]
# lst.sort()
# print("The second highest number is:",lst[-2])




def CodelandUsernameValidation(strParam):

  if len(strParam) < 4 or len(strParam) > 25:
    return False

  if not strParam[0].isalpha():
    return False
  
  if not (strParam.isalnum() and '_' in strParam):
    print(strParam.isalnum())
    print('_' in strParam)
    return False

  if strParam[-1] == '_':
    return False



  # code goes here
  return True

# keep this function call here 
print(CodelandUsernameValidation(input()))







