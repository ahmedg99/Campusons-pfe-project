  
from django.urls import path
from . import views
urlpatterns = [
    path('homee/', views.homee, name='homee'),
    path('listing/', views.listing, name='listing'),
    path('annonce/<int:annonce_id>/', views.annonce,name='annonce'),
    path('annonce/new/', views.annonce_new, name='annonce_new'),
    path('annonce/annonce_a_approuver/', views.annonce_a_approuver, name='annonce_a_approuver'),
    path('annonce/annonce_a_approuver/delete/<int:annonce_id>', views.delete_annonce, name='delete_annonce_a_approuver'),
    path('annonce/delete/<int:annonce_id>', views.delete_annonceapp, name='delete_annonce'),
    path('recherche/', views.recherche, name='recherche'),
    path('annonce/annonce_a_approuver/approuve/<int:annonce_id>',views.approuver_annonce,name='approuver_annonce')
    
]




  
