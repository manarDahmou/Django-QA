import pytest
import django
from django.conf import settings

# Assurez-vous que Django est correctement configuré avant d'importer les modèles
django.setup()

from employee.models import Employee

@pytest.mark.django_db
def test_create_employee():
    employee = Employee.objects.create(
        eid="E001",
        ename="John Doe",
        eemail="johndoe@example.com",
        econtact="9876543210"
    )
    assert employee.eid == "E001"
    assert employee.ename == "John Doe"
    assert employee.eemail == "johndoe@example.com"
    assert employee.econtact == "9876543210"
