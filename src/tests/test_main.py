import unittest
from main import main
from peli import Pelialusta
import os

class TestMain(unittest.TestCase):
    def SetUp(self):
        self.alusta = Pelialusta()

    def test_main(self):
        self.SetUp()
        result = os.system("main.py")
        if result:
            print("Integration test failed!")
        else:
            print("väärä komento")