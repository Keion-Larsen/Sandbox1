'''

Keion Larsen

'''

enteredPass = str(input("Entered Password: "))
if len(enteredPass) < 2:
    enteredPass = str(input("Please Enter Valid Password: "))

length = len(enteredPass)
for i in range(length):
    asterisks = '*'
    print(asterisks.rstrip("/n"))
