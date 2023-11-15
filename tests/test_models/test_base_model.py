from models import base_model
import unittest

mod_doc = base_model.__doc__
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the baseModel class"""
    def test_instantiation(self):
        """Check if the Object is correctly instantiated"""
        obj = BaseModel()
        self.assertIs(type(obj), BaseModel)
    
    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(mod_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(mod_doc) > 1,
                        "base_model.py needs a docstring")


if __name__ == "__main__":
    unittest.main()