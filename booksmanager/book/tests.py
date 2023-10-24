from django.test import TestCase

# Create your tests here.
import os.path

class PeopleInfo():
    name = "111"
    age = "dddd"
    def showInfo(self):
        print(self.name)


p = PeopleInfo()
print(p.showInfo())