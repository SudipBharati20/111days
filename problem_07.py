#Write a program to find out whether a given post is talking about “Sudip” or not

post = input("Enter your post: ").lower()
if "sudip" in post:
    print("Yes")
else:
    print("No")