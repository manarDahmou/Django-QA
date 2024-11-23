import pytest
from employee.models import Employee

@pytest.mark.django_db
def test_create_employee():
    # Créer un employé avec des données spécifiques
    employee = Employee.objects.create(
        eid="E001",
        ename="John Doe",
        eemail="johndoe",
        econtact="9876543210"
    )

    # Vérifiez que les données sont correctement enregistrées
    assert employee.eid == "E001"
    assert employee.ename == "John Doe"
    assert employee.eemail == "johndoe@example.com"
    assert employee.econtact == "9876543210"
