# AirBnB clone
A clone for the well-known AirBnB website implemented in `python 3`; currently in development. This is a step towards building my first full stack web application

## Features:
- The Console - create and manage objects via CLI
- Storage Engine - abstracted storage engine
- Models - Classes and Object hierarchy (OOP inheritance)
- Unit test - validate models and storage engine using python unittest module

### The console
The console (`console.py`) is similar to other well known command line interface. For this project, we want to be able to manage the objects of our project
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from storage
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

The following commands are available for the console interpreter
 - `help` - display list of available commands
 - `help <command>`: display documentation for <command>
 - `quit` - exit the console
 - `EOF` - exit the console
 - `create <className>`: create a new instance of a given class
 - `show <className> <id>`: display an instance of class `<className>` with id `<id>`
 - `destroy <className> <id>`: delete an instance of class `<className>` with id `<id>`
 - `all <className>`: dipslay all instance of class `<className>`
 - `update <className>`: updates an instance based on the class name and id `e.g`: `update User 12x34y45z name Kennedy`
 - `<className>.<command>(<args>)` - perform `<command>` on all instance of class `<className>`. Example: `User.count()` - displays total number of Users in storage. available commands include:
    - `count` - get total of instance of a class
    - `show(<id>)` - display instance of a class given an id
    - `all` - display all instance of a class
    - `destroy(<id>)` - delete an instance given the <id>
    - `update(<args>)` - update an instance

### Example
```bash
obimbasmart@MyXubuntu:~/alx-repos/AirBnB_clone$ ./console.py
(hbnb) help create
Creates a new instance of "arg"
(hbnb) create User
2774e6a9579143b49e6b9f46199d826d
(hbnb) show User 2774e6a9579143b49e6b9f46199d826d
[User] (2774e6a9579143b49e6b9f46199d826d) {'id': '2774e6a9579143b49e6b9f46199d826d', 'created_at': datetime.datetime(2023, 11, 5, 5, 15, 27, 301396), 'updated_at': datetime.datetime(2023, 11, 5, 5, 15, 27, 301462)}
(hbnb) User.show(2774e6a9579143b49e6b9f46199d826d)
[User] (2774e6a9579143b49e6b9f46199d826d) {'id': '2774e6a9579143b49e6b9f46199d826d', 'created_at': datetime.datetime(2023, 11, 5, 5, 15, 27, 301396), 'updated_at': datetime.datetime(2023, 11, 5, 5, 15, 27, 301462)}
(hbnb) 
(hbnb) create User
29a168974e584f26a7e5b658c9fefd1d
(hbnb) 
(hbnb) User.count()
2
(hbnb) (hbnb) destroy User 2774e6a9579143b49e6b9f46199d826d
(hbnb) User.show(2774e6a9579143b49e6b9f46199d826d)
** no instance found **
(hbnb) all User
["[User] (29a168974e584f26a7e5b658c9fefd1d) {'id': '29a168974e584f26a7e5b658c9fefd1d', 'created_at': datetime.datetime(2023, 11, 5, 5, 16, 49, 706721), 'updated_at': datetime.datetime(2023, 11, 5, 5, 16, 49, 706775)}"]
(hbnb) update User 29a168974e584f26a7e5b658c9fefd1d name JohnKennedy
(hbnb) User.show(29a168974e584f26a7e5b658c9fefd1d)
[User] (29a168974e584f26a7e5b658c9fefd1d) {'id': '29a168974e584f26a7e5b658c9fefd1d', 'created_at': datetime.datetime(2023, 11, 5, 5, 16, 49, 706721), 'updated_at': datetime.datetime(2023, 11, 5, 5, 21, 33, 554893), 'name': 'JohnKennedy'}
(hbnb) quit
obimbasmart@MyXubuntu:~/alx-repos/AirBnB_clone$
```

### Models and design
```
BaseModel    <!--base class->
|
|
| ____ User 
| ____ City
| ____ Amenities
.
.
``````

### Storage Engine

 The storage engine has been reimplemented to allow transition between FileStorage and DBStorage:  The abstraction makes it easy to change storage type  without knowing how it’s stored.

- #### File storage
```
<class 'BaseModel'>
.  to_dict()
    .  <class 'dict'>
        . JSON dump
            . <class 'str'>
                . FILE
            . <class 'str'>
        . JSON load
    . <class 'dict'>
<class 'BaseModel'>
```

- #### DB storage

<div align=center>
<img src  = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/daaef631636b40e0a279a8f240703e065f9d3481.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231211T134008Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cf1eb5871dd5ba6807b7ed6f7ac55a40c426e155edab9a74cfdb531e82686d6f">
</div>

The DataBase(DB) storage is implemeneted using `MYSQL` and the `SQLAlchemy` library which maps objects to Database storage


## Dependencies
- Python3.x

## Usage and Installation
This project can be executed as a command line interpreter. To use:
- clone the repository:
```bash
git clone git@github.com:obimbasmart/AirBnB_clone.git
```
- navigate to the root folder
```
cd AirBnB_clone
```
- start the console
```
obimbasmart@MyXubuntu:~/alx-repos/AirBnB_clone$ python3 console.py
```

## Testing
All tests are located in the `tests/` folder. To run the test:
```
python -m unittest discover tests
```














