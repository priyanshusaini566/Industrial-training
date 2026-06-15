"""
Student Name (Easy) Create a class Student with a private variable _name.

Write a set_name() method to assign a name.
Write a get_name() method to return the name.
Create an object, set name as “Mahi”, and print it.
"""

class Student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

s1=Student()
s1.set_name("priyanshu")
s1.get_name()