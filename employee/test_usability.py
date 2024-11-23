# import pytest
# from django.test import Client

# @pytest.mark.django_db
# def test_page_structure():
#     """Vérifie que la page a une structure correcte et contient un titre <h1>."""
#     client = Client()
#     response = client.get('/emp/')  # URL du formulaire pour ajouter un employé

#     html_content = response.content.decode()

#     # Vérifie que la page contient un titre <h1>
#     assert '<h1>' in html_content, "La page doit contenir un titre <h1>"
#     assert '<h1></h1>' not in html_content, "Le titre <h1> ne doit pas être vide"

# @pytest.mark.django_db
# def test_form_fields():
#     """Vérifie que le formulaire a des champs correctement étiquetés et fonctionne correctement."""
#     client = Client()
#     response = client.get('/emp/')  # URL du formulaire pour ajouter un employé

#     html_content = response.content.decode()

#     # Vérifie que chaque champ de formulaire a un label associé
#     assert '<label for="id_eid">' in html_content, "Le champ 'eid' doit avoir un label"
#     assert '<label for="id_ename">' in html_content, "Le champ 'ename' doit avoir un label"
#     assert '<label for="id_eemail">' in html_content, "Le champ 'eemail' doit avoir un label"
#     assert '<label for="id_econtact">' in html_content, "Le champ 'econtact' doit avoir un label"

# @pytest.mark.django_db
# def test_form_submission():
#     """Vérifie que le formulaire fonctionne correctement et redirige après soumission."""
#     client = Client()

#     # Soumettre des données valides
#     data = {
#         'eid': 'E001',
#         'ename': 'John Doe',
#         'eemail': 'john.doe@example.com',
#         'econtact': '1234567890'
#     }
#     response = client.post('/emp/', data)

#     # Vérifie si la redirection vers la page de confirmation (show) a lieu après soumission
#     assert response.status_code == 302  # Redirection attendue après soumission
#     assert response.url == '/show'  # Redirection attendue vers la page de show

# @pytest.mark.django_db
# def test_form_validation_error():
#     """Vérifie que des erreurs de validation sont affichées si le formulaire est soumis avec des données invalides."""
#     client = Client()

#     # Soumettre des données invalides (par exemple, un email mal formaté)
#     data = {
#         'eid': 'E001',
#         'ename': 'John Doe',
#         'eemail': 'invalid-email',  # Email invalide
#         'econtact': '1234567890'
#     }
#     response = client.post('/emp/', data)

#     # Vérifie que la page contient un message d'erreur pour le champ 'eemail'
#     html_content = response.content.decode()
#     assert "Enter a valid email address." in html_content, "Le message d'erreur d'email n'est pas affiché correctement"
