#!/usr/bin/python3
"""
unittest class for Amenity module
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    unittest class for Amenity module
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

    def test_no_args_instances(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_pub_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_pub_dt(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_pub_dt(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_pub_attr(self):
        am1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am1.__dict__)

    def test_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_unique_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_uinque_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_represent(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        am1 = Amenity()
        am1.id = "123456"
        am1.created_at = am1.updated_at = my_date
        amenity_str = am1.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + my_date_repr, amenity_str)
        self.assertIn("'updated_at': " + my_date_repr, amenity_str)

    def test_args_unused(self):
        am1 = Amenity(None)
        self.assertNotIn(None, am1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        instantiation with kwargs test method
        """
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        am1 = Amenity(id="1234", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(am1.id, "1234")
        self.assertEqual(am1.created_at, my_date)
        self.assertEqual(am1.updated_at, my_date)


if __name__ == "__main__":
    unittest.main()