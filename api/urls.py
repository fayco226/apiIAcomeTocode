from django.urls import path
from .views import save_apels

urlpatterns = [
    path('api/apels/', save_apels, name='save-apels'),
    # Autres URLs de votre application
]
