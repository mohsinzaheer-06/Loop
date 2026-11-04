Email = "abc@gmail.com"
Password = "123456"

while True:
    user_email = input("Enter your Email: ")
    user_password = input("Enter your Password: ")
    if (Email  == user_email and Password == user_password):
        print("Access Granted")
        break
    else:
        print("Email or password maybe wrong")


