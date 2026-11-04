Email = "abc@gmail.com"
Password = "123456"

while True:
    user_email = input("Enter your Email: ")
    user_password = input("Enter your Password: ")

    if (Email  == user_email):
        print("Email Accpeted")    
    else:
        print("Email is wrong")

    if (Password  == user_password):
        print("Correct Password")    
    else:
        print("Password is wrong")
    
    if(Email  == user_email and Password == user_password):
        print("Access Granted")
        break
    else:
        print("Email or password maybe wrong")