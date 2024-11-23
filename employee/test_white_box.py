import pytest
from django.test import Client
from employee.models import Employee

@pytest.mark.django_db
def test_emp_view_valid_data():
    """Test de la vue emp avec des données valides."""
    client = Client()

    data = {
        'eid': 'E001',
        'ename': 'John Doe',
        'eemail': 'john.doe@example.com',
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)

    # Vérifier la création d'un employé et la redirection vers '/show'
    assert response.status_code == 302  # Redirection vers '/show' après la soumission
    assert Employee.objects.count() == 1  # Vérifier qu'un employé a été ajouté à la base de données
    assert Employee.objects.first().ename == 'John Doe'  # Vérifier que le nom de l'employé correspond à l'entrée

@pytest.mark.django_db
def test_emp_view_invalid_data():
    """Test de la vue emp avec des données invalides (email invalide)."""
    client = Client()

    data = {
        'eid': 'E001',
        'ename': 'John Doe',
        'eemail': 'invalid-email',  # Email invalide
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)

    # Vérifier que le formulaire n'est pas validé et que l'utilisateur reste sur la même page
    assert response.status_code == 200  # La page devrait être rechargée en cas d'erreur
    assert "Enter a valid email address." in response.content.decode()  # Vérifier le message d'erreur pour l'email
    assert Employee.objects.count() == 0  # Aucun employé ne devrait être ajouté à la base de données

@pytest.mark.django_db
def test_emp_view_missing_field():
    """Test de la vue emp avec un champ obligatoire manquant (eid)."""
    client = Client()

    data = {
        'eid': '',  # Champ obligatoire vide
        'ename': 'John Doe',
        'eemail': 'john.doe@example.com',
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)

    # Vérifier que le formulaire n'est pas validé et que des erreurs sont affichées
    assert response.status_code == 200  # La page devrait être rechargée en cas d'erreur
    assert "This field is required." in response.content.decode()  # Vérifier le message d'erreur pour le champ 'eid'
    assert Employee.objects.count() == 0  # Aucun employé ne devrait être ajouté à la base de données
