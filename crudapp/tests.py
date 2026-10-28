
from django.test import TestCase
from .models import Department, Employee


class EmployeeDepartmentTests(TestCase):

    def test_employee_department_relation(self):
        department = Department.objects.create(name="IT")

        employee = Employee.objects.create(
            name="Test",
            age=25,
            department=department,
            gender="Other",
            email="test@example.com"
        )

        self.assertEqual(employee.department.name, "IT")
