from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='loginahmed.html'),name='login'),
    path('enetcom/',views.enetcom,name='enetcom'),
    path('isims/',views.isims,name='isims'),
    path('isgi/',views.isgi,name='isgi'),
    path('isms/',views.isms,name='isms'),


    path('cafés/',views.cafés,name='cafés'),
    path('restaurants/',views.restaurants,name='restaurants'),
    path('mosquées/',views.mosquées,name='mosquées'),
    path('supermarchés/',views.supermarchés,name='supermarchés'),
    path('centre/',views.centre,name='centre'),
    path('bib/',views.bib,name='bib'),
    path('clubenetcom/',views.clubenetcom,name='clubenetcom'),
    path('manifestation/',views.manifestation,name='manifestation'),
    



    path('foyersetatique/',views.foyersetatique,name='foyersetatique'),
    path('register/',views.register,name='register'),
    path('base/',views.base,name='base'),
    path('nouvelleannonce/',views.nouvelleannonce,name='nouvelleannonce'),
    path('clubs/',views.clubs,name='clubs'),
    path('profile/',views.profile,name='profile'),
    path('profile/annonces/',views.profile_annonces,name='profileannonces'),
    path('profile/edit/',views.profile_edit,name='editprofile'),
    path('profile/annonces/edit/<int:annonce_id>',views.edit_annonce,name='editannonce'),
    path('profile/deleteannonceprof/<int:annonce_id>',views.delete_annonceprof,name='deleteannonceprof'),
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change'),
    path('settings/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),

    



    path('question/',views.askQuestion,name="askquestion"),
    path('reponsequestion/',views.reponsequestion,name="reponse"),
    path('reponse/',views.reponse,name="reponses"),
]
