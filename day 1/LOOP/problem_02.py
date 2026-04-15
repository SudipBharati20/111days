#Write a program to greet all the person names stored in a list ‘l’ and which starts
#with S.
l1 = ["Sher", "Sunny", "Rahul", "Sakshi"]

for name in l1:
    if name.startswith("S"):
        print(f"Hello, {name}!")