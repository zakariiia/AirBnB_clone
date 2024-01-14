#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
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

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(inst_plce))
        self.assertNotIn("city_id", inst_plce.__dict__)

    def test_user_id_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(inst_plce))
        self.assertNotIn("user_id", inst_plce.__dict__)

    def test_name_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(inst_plce))
        self.assertNotIn("name", inst_plce.__dict__)

    def test_description_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(inst_plce))
        self.assertNotIn("desctiption", inst_plce.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(inst_plce))
        self.assertNotIn("number_rooms", inst_plce.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(inst_plce))
        self.assertNotIn("number_bathrooms", inst_plce.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(inst_plce))
        self.assertNotIn("max_guest", inst_plce.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(inst_plce))
        self.assertNotIn("price_by_night", inst_plce.__dict__)

    def test_latitude_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(inst_plce))
        self.assertNotIn("latitude", inst_plce.__dict__)

    def test_longitude_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(inst_plce))
        self.assertNotIn("longitude", inst_plce.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        inst_plce = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(inst_plce))
        self.assertNotIn("amenity_ids", inst_plce.__dict__)

    def test_two_places_unique_ids(self):
        inst_plce1 = Place()
        inst_plce2 = Place()
        self.assertNotEqual(inst_plce1.id, inst_plce2.id)

    def test_two_places_different_created_at(self):
        inst_plce1 = Place()
        sleep(0.05)
        inst_plce2 = Place()
        self.assertLess(inst_plce1.created_at, inst_plce2.created_at)

    def test_two_places_different_updated_at(self):
        inst_plce1 = Place()
        sleep(0.05)
        inst_plce2 = Place()
        self.assertLess(inst_plce1.updated_at, inst_plce2.updated_at)

    def test_str_represent(self):
        inst_date = datetime.today()
        inst_date_repr = repr(inst_date)
        inst_plce = Place()
        inst_plce.id = "123456"
        inst_plce.created_at = inst_plce.updated_at = inst_date
        inst_plce_str = inst_plce.__str__()
        self.assertIn("[Place] (123456)", inst_plce_str)
        self.assertIn("'id': '123456'", inst_plce_str)
        self.assertIn("'created_at': " + inst_date_repr, inst_plce_str)
        self.assertIn("'updated_at': " + inst_date_repr, inst_plce_str)

    def test_args_unused(self):
        inst_plce = Place(None)
        self.assertNotIn(None, inst_plce.__dict__.values())

    def test_kwargs(self):
        inst_date = datetime.today()
        inst_date_iso = inst_date.isoformat()
        inst_plce = Place(id="1234", created_at=inst_date_iso, updated_at=inst_date_iso)
        self.assertEqual(inst_plce.id, "1234")
        self.assertEqual(inst_plce.created_at, inst_date)
        self.assertEqual(inst_plce.updated_at, inst_date)

if __name__ == "__main__":
    unittest.main()