#!/usr/bin/python3

"""This module instantiates an object of class FileStorage
Or object of DBStorage depending on the value of the enviroment
variable HBNB_TYPE_STORAGE"""

import os

DB_TYPE = os.getenv("HBNB_TYPE_STORAGE")

if DB_TYPE == "file":
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

elif DB_TYPE == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
