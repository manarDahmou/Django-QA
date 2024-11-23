# from django.contrib import admin  
# from django.urls import path  
# from employee import views  

# urlpatterns = [  
#     path('admin/', admin.site.urls),  
#     path('emp', views.emp),  
#     path('show',views.show),  
#     path('edit/<int:id>', views.edit),  
#     path('update/<int:id>', views.update),  
#     path('delete/<int:id>', views.destroy),  
# ]  
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/', views.emp),  # Ajoutez le '/' final
    path('show/', views.show),  # Ajoutez le '/' final
    path('edit/<int:id>/', views.edit),  # Ajoutez le '/' final
    path('update/<int:id>/', views.update),  # Ajoutez le '/' final
    path('delete/<int:id>/', views.destroy),  # Ajoutez le '/' final
]
