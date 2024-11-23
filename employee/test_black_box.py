import pytest
from django.test import Client

@pytest.mark.django_db
def test_form_submission_valid_data():
    """Test de soumission du formulaire avec des données valides"""
    client = Client()

    # Soumettre des données valides
    data = {
        'eid': 'E001',
        'ename': 'John Doe',
        'eemail': 'john.doe@example.com',
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)

    # Vérifier si la redirection vers la page de confirmation (show) a lieu après soumission
    assert response.status_code == 302  # Redirection attendue après soumission
    assert response.url == '/show'  # La redirection attendue vers la page de show

@pytest.mark.django_db
def test_form_submission_invalid_email():
    """Test de soumission du formulaire avec un email invalide"""
    client = Client()

    # Soumettre des données avec un email invalide
    data = {
        'eid': 'E001',
        'ename': 'John Doe',
        'eemail': 'invalid-email',  # Email invalide
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)

    # Vérifier que la page contient un message d'erreur pour le champ 'eemail'
    html_content = response.content.decode()
    assert "Enter a valid email address." in html_content, "Le message d'erreur d'email n'est pas affiché correctement"

@pytest.mark.django_db
def test_form_submission_missing_required_field():
    """Test de soumission du formulaire avec un champ manquant"""
    client = Client()

    # Soumettre des données sans remplir le champ 'eid' (champ requis)
    data = {
        'eid': '',  # Champ obligatoire vide
        'ename': 'John Doe',
        'eemail': 'john.doe@example.com',
        'econtact': '1234567890'
    }
    response = client.post('/emp/', data)

    # Vérifier que le formulaire affiche un message d'erreur pour le champ 'eid'
    html_content = response.content.decode()
    assert "This field is required." in html_content, "Le message d'erreur pour le champ 'eid' n'est pas affiché"

@pytest.mark.django_db
def test_form_submission_with_empty_fields():
    """Test de soumission du formulaire avec tous les champs vides"""
    client = Client()

    # Soumettre un formulaire avec tous les champs vides
    data = {
        'eid': '',
        'ename': '',
        'eemail': '',
        'econtact': ''
    }
    response = client.post('/emp/', data)

    # Vérifier que des erreurs sont affichées pour tous les champs obligatoires
    html_content = response.content.decode()
    assert "This field is required." in html_content, "Les messages d'erreur pour les champs obligatoires ne sont pas affichés"

@pytest.mark.django_db
def test_page_load():
    """Test pour vérifier si la page de formulaire se charge correctement."""
    client = Client()
    response = client.get('/emp/')
    
    # Vérifier que la page de formulaire se charge avec un code de statut 200 (OK)
    assert response.status_code == 200, "La page de formulaire ne se charge pas correctement"
