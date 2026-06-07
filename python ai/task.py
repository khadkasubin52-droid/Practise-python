a = input("Enter the name: ")
 
if a.lower() =="subin":
    print("Name is correct: ")

    b= int(input("Enter the date of birth: "))
    print("The date of birth is " + str(b))

    c= int(input("Enter the current date: "))

    d = c - b 
    print("the difference is: " + str(d))

    sum= d + 10
    print("Your age after 10 years will be:" +str(sum))

else:
    print("Try again")





