from django.urls import path
from .views import home1, fornecedor


urlpatterns = [
    path('', home1 ),
    path('fornecedor/<int:codigo>/', fornecedor),

]