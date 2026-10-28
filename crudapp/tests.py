from django.test import TestCase
from .models import Department, Employee
class EmployeeDepartmentTests(TestCase):
    def test_employee_department_relation(self):
        d=Department.objects.create(name="IT")
        e=Employee.objects.create(name="Test",age=25,department=d,gender="Other",email="test@example.com")
        self.assertEqual(e.department.name,"IT")
