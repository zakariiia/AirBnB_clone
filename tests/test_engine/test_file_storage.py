#!/usr/bin/python3
"""
Unittest class for FileStorage model
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """
    Testing instances.
    """
    
    def setUp(self):
        try:
            os.rename("file.json", "file_tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("file_tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_file_storage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_storage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_storage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """
    Testing methods.
    """

    def setUp(self):
        try:
            os.rename("file.json", "file_tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("file_tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}


    def test_new(self):
        u_ser = User()
        s_tate = State()
        p_lace = Place()
        c_ity = City()
        a_menity = Amenity()
        r_eview = Review()
        models.storage.new(u_ser)
        models.storage.new(s_tate)
        models.storage.new(p_lace)
        models.storage.new(c_ity)
        models.storage.new(a_menity)
        models.storage.new(r_eview)
        self.assertIn("User." + u_ser.id, models.storage.all().keys())
        self.assertIn(u_ser, models.storage.all().values())
        self.assertIn("State." + s_tate.id, models.storage.all().keys())
        self.assertIn(s_tate, models.storage.all().values())
        self.assertIn("Place." + p_lace.id, models.storage.all().keys())
        self.assertIn(p_lace, models.storage.all().values())
        self.assertIn("City." + c_ity.id, models.storage.all().keys())
        self.assertIn(c_ity, models.storage.all().values())
        self.assertIn("Amenity." + a_menity.id, models.storage.all().keys())
        self.assertIn(a_menity, models.storage.all().values())
        self.assertIn("Review." + r_eview.id, models.storage.all().keys())
        self.assertIn(r_eview, models.storage.all().values())

    def test_save(self):
        u_ser = User()
        s_tate = State()
        p_lace = Place()
        c_ity = City()
        a_menity = Amenity()
        r_eview = Review()
        models.storage.new(u_ser)
        models.storage.new(s_tate)
        models.storage.new(p_lace)
        models.storage.new(c_ity)
        models.storage.new(a_menity)
        models.storage.new(r_eview)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("User." + u_ser.id, save_text)
            self.assertIn("State." + s_tate.id, save_text)
            self.assertIn("Place." + p_lace.id, save_text)
            self.assertIn("City." + c_ity.id, save_text)
            self.assertIn("Amenity." + a_menity.id, save_text)
            self.assertIn("Review." + r_eview.id, save_text)


    def test_reload(self):
        u_ser = User()
        s_tate = State()
        p_lace = Place()
        c_ity = City()
        a_menity = Amenity()
        r_eview = Review()
        models.storage.new(u_ser)
        models.storage.new(s_tate)
        models.storage.new(p_lace)
        models.storage.new(c_ity)
        models.storage.new(a_menity)
        models.storage.new(r_eview)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("User." + u_ser.id, objs)
        self.assertIn("State." + s_tate.id, objs)
        self.assertIn("Place." + p_lace.id, objs)
        self.assertIn("City." + c_ity.id, objs)
        self.assertIn("Amenity." + a_menity.id, objs)
        self.assertIn("Review." + r_eview.id, objs)


if __name__ == "__main__":
    unittest.main()
