AVAILABLE COMMANDS
------------------

Before Login:
- register - Register a new user account
- login <url> - Login to the service (URL format: example.pythonanywhere.com/api/)
- list - View a list of all module instances and the professors teaching them
- view - View the ratings of all professors
- average <professor_id> <module_code> - View the average rating of a specific professor for a specific module
- h or help - Display available commands
- q or quit or exit - Exit the application

After Login:
- All previous commands (except login and register)
- rate <professor_id> <module_code> <year> <semester> <rating> - Rate a professor for a specific module instance
- logout - Log out from the current session

COMMANDS DESCRIPTIONS
---------------------

register:
  Used to allow a user to register with the service using a username, email, and password.
  Syntax: register

login:
  Used to log in to the service.
  Syntax: login <url>
  Example: login https://sc22hn.pythonanywhere.com/api/login/

logout:
  Causes the user to logout from the current session.
  Syntax: logout

list:
  Used to view a list of all module instances and the professors teaching each of them.
  Syntax: list

view:
  Used to view the rating of all professors.
  Syntax: view

average:
  Used to view the average rating of a specific professor in a specific module.
  Syntax: average <professor_id> <module_code>
  Example: average HN1 SS1

rate:
  Used to rate the teaching of a certain professor in a certain module instance.
  Syntax: rate <professor_id> <module_code> <year> <semester> <rating>
  Example: rate HN1 SS1 2024 1 5
  Note: Rating must be an integer between 1-5

DOMAIN
------
sc22hn.pythonanywhere.com

SUB-DOMAINS
-----------
Admin page: /admin/

API functions:

1) Register: /api/register/
2) Login: /api/login/
3) List: /api/list_modules/
4) View: /api/view/
5) Average: /api/average/
6) Log-out: /api/logout/
7) Rate: /api/rate/

ADMIN CREDENTIALS
-----------------
Username: sc22hn
Password: 1 (Easy password for ease of testing)

NOTES
-----
- Users must be logged in before they can submit ratings
- Users can only rate a professor for a module instance once
- '/' Automatically appended to URL in login function since it is required for post requests
