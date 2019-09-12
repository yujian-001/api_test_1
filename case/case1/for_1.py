import unittest
class run1(unittest.TestCase):
    def setUp(self):
        print("---setUP---")
    def tearDown(self):
        print("---tearDown---")
    def test_01(self):
        self.assertIn("a","abc",msg="不存在包含关系")