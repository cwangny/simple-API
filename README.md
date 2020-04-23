# REST API Project with CRUD Functionality

This is a simple API that stores name, address and phone number of a user. It allows you to create, read, update and delete the users in the database and the data is serialized in JSON.

By - Mison Caamwang  
## 1. Install all dependencies:
#### Install the following python packages first using ```pip3```
Install globally or use virtual environment or pipenv 
- flask
- flask_sqlalchemy
- flask_marshmallow

## 2. Create and Setup the Database:

1. Open a new terminal and open python shell in your project folder:
```bash
python3
```
2. Run this code in the shell:
```python
from server import db
```
```python
db.create_all()
```

A new file *db.sqlite3* will be created in the project folder.

## 3. Run the server
1. Run this command:
```bash
python3 server.py
```

## 4. Use POSTMAN to test: [POST, GET, PUT, DELETE]. 

Data is serialised into JSON (example 1):
```JSON
{
    "name": "Tony Stark",
    "address": "Malibu Point 10880, Malibu, California 90265",
    "phone": 6781367092
}
```
### Routes:
- [{URL}/user]() is the entry point. (URL is provided by the server)
### Adding a user:
- To add a user to the database, send a **POST** request to [/user]() in raw JSON format like example 1. 
- All 3 keys must have a value.   

### Get all users:
- To get a list of all the users in the databse, send a **GET** request to [/user]()

### Search by user's name:
- To search for a user, add the search parameter(name) [/user/{SearchParameter}]() and send a **GET** request. This will return a list of **ID**'s which matches the name. 

* Example:
    * Suppose there are two users with name = "Tony"
    * Put in the parameters [/user/Tony]() and send a **GET** request
    * The following list is returned. There are two users with name = "Tony" and their **ID** in the database in **1** and **2**:
```
ID: [<User 1>, <User 2>]
```

### Update user's information:
* Use the **ID** to display information of a single User. Example: Sending a **GET** request to [/1]() will return the information of the first Tony. Similarly, [/2]() will return the information of the second Tony.

* **ID** is also used to update the information by sending a **PUT** request to [/{id}]() to change "name", "address" or "phone". 
    * Example: Update information for User with **ID** 1.
    * Send a **PUT** request to [/1]() with raw JSON format:
    ```JSON
    {
        "name": "Pepper Potts",
        "address": "Malibu Point 10880, Malibu, California 90265",
        "phone": 911
    }
    ```

### Delete a user:
* A user can be removed from the database by sending a **DELETE** request to [/{id}](). 
    * Example: Delete a user with **ID** 1.
    * Send **DELETE** request to [/1]()


