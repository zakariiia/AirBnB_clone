#!/usr/bin/python3
"""
Testing Review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unittests for testing Review.
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
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(rev.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(rev.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(rev.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_two_reviews_unique_ids(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_two_reviews_different_created_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_two_reviews_different_updated_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_str_representation(self):
        ins_date = datetime.today()
        ins_date_repr = repr(ins_date)
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = ins_date
        rev_str = rev.__str__()
        self.assertIn("[Review] (123456)", rev_str)
        self.assertIn("'id': '123456'", rev_str)
        self.assertIn("'created_at': " + ins_date_repr, rev_str)
        self.assertIn("'updated_at': " + ins_date_repr, rev_str)

    def test_args_unused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_instantiation_with_kwargs(self):
        ins_date = datetime.today()
        ins_date_iso = ins_date.isoformat()
        rev = Review(id="1234", created_at=ins_date_iso, updated_at=ins_date_iso)
        self.assertEqual(rev.id, "1234")
        self.assertEqual(rev.created_at, ins_date)
        self.assertEqual(rev.updated_at, ins_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()