userInput=input("enter character: ")
if userInput.isnumeric()==True :
      check=False
elif userInput.isnumeric()!=True:
      check=True
if check==True:
    y = userInput.upper()
    x = (ord(y))
    t = x - 64
    r=str(t)
    print(r)
else:
    print("not a valid input")