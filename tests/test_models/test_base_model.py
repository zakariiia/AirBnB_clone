#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from models.base_model import BaseModel



class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "file_tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("file_tmp.json", "file.json")
        except FileNotFoundError:
            pass
    def test_init(self):
        """
        Test for init
        """
        mod1 = BaseModel()

        self.assertIsNotNone(mod1.id)
        self.assertIsNotNone(mod1.created_at)
        self.assertIsNotNone(mod1.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        mod1 = BaseModel()

        initial_updated_at = mod1.updated_at

        current_updated_at = mod1.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        mod1 = BaseModel()

        mod1_dict = mod1.to_dict()

        self.assertIsInstance(mod1_dict, dict)
        self.assertEqual(mod1_dict["__class__"], 'BaseModel')
        self.assertEqual(mod1_dict['id'], mod1.id)
        self.assertEqual(mod1_dict["updated_at"], mod1.created_at.isoformat())
        self.assertEqual(mod1_dict['created_at'], mod1.created_at.isoformat())
        


    def test_str(self):
        """
        Test for string representation
        """
        mod1 = BaseModel()

        self.assertTrue(str(mod1).startswith('[BaseModel]'))
        self.assertIn(str(mod1.__dict__), str(mod1))
        self.assertIn(mod1.id, str(mod1))


if __name__ == "__main__":
    unittest.main()
