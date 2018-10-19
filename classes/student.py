import csv 
import os.path
from classes.person import Person

class Student(Person):

  def __init__(self, school_id):
    self.school_id = school_id

  @classmethod
  def objects(cls):
    students = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/students.csv")
    
    with open(path) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        students.append(Student(dict(row)))
    
    return students



