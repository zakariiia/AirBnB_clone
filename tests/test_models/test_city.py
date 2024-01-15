#!/usr/bin/python3
"""
testing City
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unittests for testing instances.
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

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_pub_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_pub_dt(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_ispub_dt(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_pub_attr(self):
        inst_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(inst_city))
        self.assertNotIn("state_id", inst_city.__dict__)

    def test_name_is_pub_attr(self):
        inst_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(inst_city))
        self.assertNotIn("name", inst_city.__dict__)

    def test_unique_id(self):
        inst_city1 = City()
        inst_city2 = City()
        self.assertNotEqual(inst_city1.id, inst_city2.id)

    def test_unique_created_at(self):
        inst_city1 = City()
        sleep(0.05)
        inst_city2 = City()
        self.assertLess(inst_city1.created_at, inst_city2.created_at)

    def test_unique_updated_at(self):
        inst_city1 = City()
        sleep(0.05)
        inst_city2 = City()
        self.assertLess(inst_city1.updated_at, inst_city2.updated_at)

    def test_str_represent(self):
        inst_date = datetime.today()
        inst_date_repr = repr(inst_date)
        inst_city = City()
        inst_city.id = "123456123456"
        inst_city.created_at = inst_city.updated_at = inst_date
        inst_city_str = inst_city.__str__()
        self.assertIn("[City] (123456123456)", inst_city_str)
        self.assertIn("'id': '123456123456'", inst_city_str)
        self.assertIn("'created_at': " + inst_date_repr, inst_city_str)
        self.assertIn("'updated_at': " + inst_date_repr, inst_city_str)


    def test_instances_with_kwargs(self):
        inst_date = datetime.today()
        inst_date_iso = inst_date.isoformat()
        inst_city = City(id="345", created_at=inst_date_iso, updated_at=inst_date_iso)
        self.assertEqual(inst_city.id, "345")
        self.assertEqual(inst_city.created_at, inst_date)
        self.assertEqual(inst_city.updated_at, inst_date)



if __name__ == "__main__":
    unittest.main()