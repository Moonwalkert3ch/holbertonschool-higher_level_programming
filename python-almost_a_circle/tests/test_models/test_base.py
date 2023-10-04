#!/usr/bin/python3
# import unittest
# from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square
"""Unittests for base.py module"""


class Test_Baseinit(unittest.TestCase):
    """Test if Base assigns unique IDs"""
    def test_uniq_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_base_custom_id(self):
        """Test if Base assigns a custom ID when provided"""
        base1 = Base(10)
        self.assertEqual(base1.id, 10)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        data = [{'key': 'value'}, {'key2': 'value2'}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"key": "value"}, {"key2": "value2"}]')

    def test_from_json_string(self):
        """Test the from_json_string method"""
        json_str = '[{"key": "value"}, {"key2": "value2"}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [{'key': 'value'}, {'key2': 'value2'}])

    def test_create(self):
        """Test the create method"""
        dummy_dict = {'id': 1, 'name': 'dummy'}
        dummy = Base.create(**dummy_dict)
        self.assertEqual(dummy.id, 1)
        self.assertEqual(dummy.name, 'dummy')

if __name__ == "__main__":
    unittest.main()
