import json


def register_user():
    username = input("Enter Username: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
        
    print("\n")
    print("Registration Successful!")

    save_to_file(username, email, password)


def save_to_file(username, email, password):
    user_data = {
        "username": username,
        "email": email,
        "password": password
    }

    try:
        try:
            with open("user_details.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):  
            data = {}
        
        data[username] = user_data
        
        with open("user_details.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\n")
        print("User details saved successfully!")
    
    except Exception as e:
        print(f"Error while saving user details: {e}")


def login_user():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        with open("user_details.json", "r") as file:
            data = json.load(file)

        if username in data and data[username]["password"] == password:
            print("\n")
            print("Login Successful!")
            return True , username
        else:
            print("\n")
            print("Invalid Username or Password.")
            return False , username

    except FileNotFoundError:
        print("\n")
        print("No registered users found. Please register first.")


def show_details(username):

    with open('user_details.json' , 'r') as file:
        data = json.load(file)
    
    # print(data[username])
    print("\n")
    print("****************  USER DETAILS  ****************")
    print("     Username : " , data[username]['username'])
    print("     Email : " , data[username]['email'])
    print("     Password : " , data[username]['password'])


def change_password(username):

    with open('user_details.json' , 'r') as file:
        data = json.load(file)

    if data[username]:
        print("\n")
        new_password = input("Enter your New Password : ")

    data[username]["password"] = new_password

    with open('user_details.json' , 'w') as file:
        json.dump(data, file, indent = 4)

    print("Password Successfully Changed")


def main():

    while True:
        print("\n")
        choice = input("Do you want to Register or Login? (R/L): ").upper()
        if choice == 'R':
            register_user()
        elif choice == 'L':
            flag , username = login_user()
            if flag:
                while True:
                    print("\n")
                    print("Enter 1 to Show User Details")
                    print("Enter 2 to Change Password")
                    print("Enter 3 to Logout")
                    print("\n")

                    num = int(input())
                    if num == 1:
                        show_details(username)
                    elif num == 2:
                        change_password(username)
                    elif num == 3:
                        break
                break
            else:
                print("Login failed. Please try again.")
        else:
            print("\n")
            print("Enter Correct Option")

    print("\nSuccessfully Exited from the System")

main()