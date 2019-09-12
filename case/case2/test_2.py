import unittest
class run1(unittest.TestCase):
    def setUp(self):
        print("---setUP---")
    def tearDown(self):
        print("---tearDown---")
    def test_02(self):
        self.assertNotIn("d","abc",msg="不存在包含关系")