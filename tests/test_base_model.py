#!/usr/bin/python3
"""Test for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Elliot"
        cls.base.my_number = 29

    def test_checking_for_docstring_BaseModel(self):
        """Checking for the class docstrings"""
        a = BaseModel().__doc__
        self.assertIsNotNone(a, msg="True")
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init_BaseModel(self):
        """Test if the base is type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_method_BaseModel(self):
        """Check if BaseModel mhave methods & they work"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_to_dict_BaseModel(self):
        """Test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['update_at'], str)

        print(self.base)


if __name__ == "__main__":
    unittest.main()
