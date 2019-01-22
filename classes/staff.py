import csv
import os.path
from classes.person import Person

class Staff(Person):
  
  def __init__(self, name, age, password, role, staff_id):
    super().__init__(name, age, password, role)
    self.staff_id = staff_id

  @classmethod
  def objects(cls):
    staff = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/staff.csv")

    with open(path) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        staff.append(Staff(**dict(row)))

    return staff

