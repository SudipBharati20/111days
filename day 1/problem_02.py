#Write a program to find out whether a student has passed or failed if it requires a
#total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
#take marks as an input from the user.

sub1 = int(input("Enter 1st subject marks: "))

sub2 = int(input("Enter 2nd subject marks: "))

sub3 = int(input("Enter 3rd subject marks: "))

if (sub1<33 or sub2 <33 or sub3<33):
    print("You are fail")
elif (sub1+sub2+sub3)/3 <40:
    print("you are fail because you got below 40%")
else:
    print("PASS")