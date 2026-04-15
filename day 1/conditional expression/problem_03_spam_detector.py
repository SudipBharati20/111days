
#A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
t#o detect these spams
comment = input("enter the text: ").lower()

if ("make a lot of money" in comment):
    spam = True
elif ("buy now" in comment):
    spam = True
elif("click this" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam")
else:
    print("This is not spam")
