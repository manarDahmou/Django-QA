import pytest
from django.test import Client
from employee.models import Employee

@pytest.mark.django_db
def test_csrf_protection():
    client = Client()

    # Créer un employé de test pour l'ajouter via le formulaire
    data = {
        'eid': 'E004',
        'ename': 'Jane Doe',
        'eemail': 'janedoe@example.com',
        'econtact': '1122334455'
    }

    # Récupérer la page du formulaire pour obtenir le token CSRF
    response = client.get('/emp/')  # URL du formulaire
    csrf_token = response.cookies['csrftoken'].value  # Extraire le token CSRF du cookie

    # Ajouter le token CSRF aux données du formulaire
    data['csrfmiddlewaretoken'] = csrf_token

    # Soumettre le formulaire avec le token CSRF
    response = client.post('/emp/', data)  # URL de création d'employé

    # Vérification que la soumission du formulaire a été acceptée
    assert response.status_code == 302  # La réponse doit être une redirection après la soumission
