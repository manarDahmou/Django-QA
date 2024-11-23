import pytest
from django.test import Client

@pytest.mark.django_db
def test_image_alt_text():
    client = Client()
    response = client.get('/emp/')  # URL du formulaire pour ajouter un employé
    
    # Vérifier la présence d'attributs alt dans les images
    html_content = response.content.decode()
    
    # Assurez-vous qu'il y a au moins une image avec l'attribut alt
    assert 'alt="' in html_content  # Vérifie la présence de l'attribut alt
    assert 'alt=""' not in html_content  # Vérifie que l'attribut alt n'est pas vide

@pytest.mark.django_db
def test_page_structure():
    client = Client()
    response = client.get('/emp/')  # URL du formulaire pour ajouter un employé
    
    html_content = response.content.decode()
    
    # Vérifier la présence d'un titre h1
    assert '<h1>' in html_content  # Vérifie qu'il y a une balise h1
    
    # Vérifier que le h1 n'est pas vide
    assert '<h1></h1>' not in html_content  # Vérifie qu'il n'y a pas de h1 vide
