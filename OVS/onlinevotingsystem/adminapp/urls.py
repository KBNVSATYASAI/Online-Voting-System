from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .views import EditVoterView

urlpatterns = [
    path('home/',views.homepage, name="homepage"),
    path('adminn/',views.navbar,name="navbar"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('votehere/',views.votehere,name="votehere"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('voteguide/',views.voteguide,name="voteguide"),
    path('user/',views.nav,name="nav"),
    path('display/',views.display,name="display"),
    path('exist/',views.exist,name="exist"),
    path('viewvoters/', views.viewvoters, name='viewvoters'),
    path('delete_voter/<int:voter_id>/', views.delete_voter, name='delete_voter'),
    path('edit_voter/<int:voter_id>/', EditVoterView.as_view(), name='edit_voter'),
]