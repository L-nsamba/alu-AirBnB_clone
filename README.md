# alu-AirBnB

This is an AirBnB clone collaborative project.

---

## Description :house:

HBnB is a complete web application, integrating database storage,  
a back-end API, and front-end interfacing in a clone of AirBnB. This is the first step towards building a full web application, an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Usage :computer:

The console works both in interactive mode and non-interactive mode, much like a Unix shell.  
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id) | ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

### Non-interactive mode example

Non-interactive mode example
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

Models

The models directory contains all the classes used in this project.

File	Description	Attributes
base_model.py	BaseModel class for all other classes	id, created_at, updated_at
user.py	User class for user information	email, password, first_name, last_name
amenity.py	Amenity class for amenity information	name
city.py	City class for city information	state_id, name
state.py	State class for state information	name
place.py	Place class for accommodation information	city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
review.py	Review class for user or host reviews	place_id, user_id, text
File Storage

The engine directory manages the serialization and deserialization of all data using JSON format.

A FileStorage class is defined in file_storage.py and follows the flow below:

<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE
-> <json string> -> JSON load -> <dictionary> -> <object>


The __init__.py file instantiates the FileStorage class as storage and calls the reload() method.
This ensures all serialized data is automatically loaded when the application starts.

Tests

All code is tested using the unittest module.
Test files are located in the tests directory.

Run all tests with:

$ python3 -m unittest discover tests


Run a specific test file with:

$ python3 -m unittest tests/test_console.py

Authors

Nkem Jeferson Achia
GitHub: https://github.com/NkemJefersonAchia

Email: j.nkem@alustudent.com

Leon Nsamba
GitHub: https://github.com/l-nsamba

Email: l.nsamba@alustudent.com
