import unittest
from app import hello_world, welcome_message

class TestHelloWorld(unittest.TestCase):

   def test_welcome_message_piyush(self):
    self.assertEqual(
        welcome_message("Piyush"),
        "Welcome to DevOps, Piyush!"
    )

def test_welcome_message_rahul(self):
    self.assertEqual(
        welcome_message("Rahul"),
        "Welcome to DevOps, Rahul!"
    )
if __name__ == "__main__":
    unittest.main()
