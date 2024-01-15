#!/usr/bin/python3
"""Testing State unittest."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instances(unittest.TestCase):
    """Test State unittest."""

    def setUp(self):
        """Test State unittest."""
        try:
            os.rename("file.json", "file_tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Test State unittest."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("file_tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instance(self):
        """Testing State unittest."""
        self.assertEqual(State, type(State()))

    def test_new_instance(self):
        """Testing State unittest."""
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_pub_str(self):
        """Testing State unittest."""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        """Testing State unittest."""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        """Testing State unittest."""
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        """Testing State unittest."""
        st = State()
        self.assertEqual(str, type(st.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test__unique_id(self):
        """Testing State unittest."""
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    def test_unique_created_at(self):
        """Testing State unittest."""
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_unique_updated_at(self):
        """Testing State unittest."""
        st1 = State()
        sleep(0.05)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    def test_str_represent(self):
        """Testing State unittest."""
        inst_date = datetime.today()
        inst_date_repr = repr(inst_date)
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = inst_date
        st_str = st.__str__()
        self.assertIn("[State] (123456)", st_str)
        self.assertIn("'id': '123456'", st_str)
        self.assertIn("'created_at': " + inst_date_repr, st_str)
        self.assertIn("'updated_at': " + inst_date_repr, st_str)

    def test_args_unused(self):
        """Testing State unittest."""
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())

    def test_kwargs(self):
        """Testing State unittest."""
        inst_date = datetime.today()
        inst_date_iso = inst_date.isoformat()
        st = State(id="345", created_at=inst_date_iso, updated_at=inst_date_iso)
        self.assertEqual(st.id, "345")
        self.assertEqual(st.created_at, inst_date)
        self.assertEqual(st.updated_at, inst_date)

    def test_instance_without_kwargs(self):
        """Testing State unittest."""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
