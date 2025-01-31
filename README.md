# Python-CLI-User_Auth
## Requirements

**Python**: Python 3.x is required. It's recommended to use a recent version for best compatibility and security.


## Libraries to Import
The script **Imports the json library***. This library is included with Python, so you don't need to install it separately.
## Code Explanation

The script implements a simple user authentication system with registration, login, viewing details, and password change functionalities.

**The script uses a Command Line Interface (CLI) for user interaction.**

```bash
register_user()
```
1. Prompts the user for a username, email, and password.
2. Prints a "Registration Successful!" message.
3. Calls save_to_file() to store the user data.



```bash
save_to_file(username, email, password)
```
1. Creates a dictionary user_data to hold the user's information.
2. Uses a try-except block to handle file operations:
* Tries to open user_details.json in read mode ("r"). If the file exists, it loads the existing JSON data into the data dictionary. If the file does not exist or if the json is corrupted, it initializes an empty dictionary data = {}. This is how we append new users without erasing the old ones.
* Adds the new user_data to the data dictionary, using the username as the key.
* Opens user_details.json in write mode ("w") and saves the updated data dictionary to the file using json.dump() with indent=4 for formatting.
3. Prints a "User details saved successfully!" message.
4. Catches any exceptions during file operations and prints an error message.

```bash
login_user()
```
1. Prompts the user for a username and password.
2. Uses a try-except block for file operations:
* Opens user_details.json in read mode and loads the data.
*  Checks if the entered username exists in the data and if the password matches.
* If login is successful, prints "Login Successful!" and returns True and the username. 
* Otherwise, prints "Invalid Username or Password." and returns False and the username.
3. Handles FileNotFoundError and prints a message if no registered users are found.

```bash
show_details(username)
```
1. Opens user_details.json in read mode. 
2. Prints the user's details (username, email, password) from the loaded data.

```bash
change_password(username)
```
1. Opens user_details.json in read mode. 
2. Prompts the user for a new password. 
3. Updates the password in the data dictionary. 
4. Opens user_details.json in write mode and saves the updated data. 
5. Prints a "Password Successfully Changed" message.

```bash
main()
```
1. The main loop: 
* Asks the user to Register (R) or Login (L). 
* Calls the appropriate function based on the user's choice. 
    * Show User Details
    * Change Password
    * Log out
* If the user logs in successfully, it enters a sub-menu to show details, change the password or logout. 
* Handles invalid input. -> Prints "Successfully Exited from the System" when the main loop ends.
## How to Run

1. **Save:** Save the code as a .py file (e.g., user_authentication.py). 
2. **Open Terminal/Command Prompt:** Open your terminal or command prompt. 
3. **Navigate:** Go to the directory where you saved the file using the cd command (e.g., cd /path/to/your/directory). 
4. **Run:** Execute the script using the command: python user_authentication.py 
5. **Interact:** The script will interact with you through the command line interface. Follow the prompts to register, login, etc.   

 
 The user_details.json file will be created in the same directory as the script when you register the first user.
