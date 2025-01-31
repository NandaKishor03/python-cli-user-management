# Python-CLI-User-Management

1. Requirements:
-> Python: Python 3.x is required. It's recommended to use a recent version for best compatibility and security. You can download Python from python.org.
-> No External Libraries: This script only uses Python's standard library, so no additional installations (like pip install ...) are needed.

2. Libraries to Import:
-> The script imports the json library. This library is included with Python, so you don't need to install it separately. Just make sure you have a working Python installation.

3. Code Explanation:
The script implements a simple user authentication system with registration, login, viewing details, and password change functionalities. User data is stored in a JSON file named user_details.json.  The script uses a Command Line Interface (CLI) for user interaction.

a.register_user():
-> Prompts the user for a username, email, and password.
-> Prints a "Registration Successful!" message.
-> Calls save_to_file() to store the user data. 

b.save_to_file(username, email, password)
-> Creates a dictionary user_data to hold the user's information.
-> Uses a try-except block to handle file operations:
      (i) Tries to open user_details.json in read mode ("r"). If the file exists, it loads the existing JSON data into the data dictionary. If the file does not exist or if the json is corrupted, it initializes an empty dictionary data = {}. This is how we append new users without erasing the old ones.
      (ii) Adds the new user_data to the data dictionary, using the username as the key.
      (iii) Opens user_details.json in write mode ("w") and saves the updated data dictionary to the file using json.dump() with indent=4 for formatting.
-> Prints a "User details saved successfully!" message.
-> Catches any exceptions during file operations and prints an error message.

c.login_user():
-> Prompts the user for a username and password.
-> Uses a try-except block for file operations:
      (i) Opens user_details.json in read mode and loads the data.
      (ii) Checks if the entered username exists in the data and if the password matches.
      (iii) If login is successful, prints "Login Successful!" and returns True and the username.
      (iv) Otherwise, prints "Invalid Username or Password." and returns False and the username.
->Handles FileNotFoundError and prints a message if no registered users are found.

d.show_details(username):
-> Opens user_details.json in read mode.
-> Prints the user's details (username, email, password) from the loaded data.

e.change_password(username):
-> Opens user_details.json in read mode.
-> Prompts the user for a new password.
-> Updates the password in the data dictionary.
->Opens user_details.json in write mode and saves the updated data.
->Prints a "Password Successfully Changed" message.

f.main():
-> The main loop:
      (i) Asks the user to Register (R) or Login (L).
      (ii) Calls the appropriate function based on the user's choice.
      (iii) If the user logs in successfully, it enters a sub-menu to show details, change the password or logout.
      (iv) Handles invalid input.
-> Prints "Successfully Exited from the System" when the main loop ends.

4. How to Run the Code:
-> Save: Save the code as a .py file (e.g., user_authentication.py).
-> Open Terminal/Command Prompt: Open your terminal or command prompt.
-> Navigate: Go to the directory where you saved the file using the cd command (e.g., cd /path/to/your/directory).
-> Run: Execute the script using the command: python user_authentication.py
-> Interact: The script will interact with you through the command line interface. Follow the prompts to register, login, etc.


The user_details.json file will be created in the same directory as the script when you register the first user.
