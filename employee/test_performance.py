import pytest
import time
from django.test import Client
from employee.models import Employee

@pytest.mark.django_db
def test_response_time():
    # Initialiser le client de test Django
    client = Client()

    # Mesurer le temps de réponse pour un GET
    start_time = time.time()
    response = client.get('/emp/')  # L'URL de la vue emp pour obtenir le formulaire
    end_time = time.time()

    response_time = end_time - start_time
    print(f"GET Response time: {response_time:.4f} seconds")
    
    # Vérifier que la réponse HTTP est correcte
    assert response.status_code == 200  # La page doit répondre correctement
    assert response_time < 1.0  # Le temps de réponse doit être inférieur à 1 seconde

    # Tester la soumission du formulaire avec un POST
    start_time = time.time()
    data = {
        'eid': 'E001',
        'ename': 'John Doe',
        'eemail': 'johndoe@example.com',
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)  # Soumettre les données via POST
    end_time = time.time()

    response_time = end_time - start_time
    print(f"POST Response time: {response_time:.4f} seconds")
    
    # Vérifier que la réponse est une redirection après soumission (statut 302)
    assert response.status_code == 302  # Redirection après la soumission du formulaire
    assert response_time < 1.0  # Le temps de réponse doit être inférieur à 1 seconde

    # Vérifier que l'employé a bien été ajouté à la base de données
    employee = Employee.objects.get(eid='E001')
    assert employee.ename == 'John Doe'
    assert employee.eemail == 'johndoe@example.com'
    assert employee.econtact == '1234567890'
