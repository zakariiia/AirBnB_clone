import json
import os
from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place



class FileStorage:

    """
    FileStorage class to store the data
    """
    __file_path = "file.json"

    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_c_nme = obj.__class__.__name__

        key = f"{obj_c_nme}.{obj.id}" # class name.idù is the key, value is the data (object)

        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}

        all_objs = FileStorage.__objects


        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        file_s = FileStorage.__file_path
        if os.path.isfile(file_s): # check If the file exist 
            with open(file_s, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        t_calss = eval(class_name)
                        # print(t_calss)

                        instc = t_calss(**value)
                        # print(instc)

                        FileStorage.__objects[key] = instc
                        # print(FileStorage.__objects)
                except Exception:
                    print("can't reload the data")
                    pass 
