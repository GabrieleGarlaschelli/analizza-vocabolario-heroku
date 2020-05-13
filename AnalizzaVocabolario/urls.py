from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from . import views

app_name = 'AnalizzaVocabolario'


urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('register', views.UserCreateView.as_view(), name='user-register'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('personalText', views.PersonalTextList, name='personal-text'),
    path('deleteText/<int:pk>', views.DeleteText.as_view(), name='delete-text'),
    path('addText', views.add_text, name='add-text'),
    path('homepage', views.Homepage, name='homepage'),
    path('search', views.search_titles, name='search'),
    path('features/<int:pk>', views.featuresText, name='features-text'),
    re_path(r'^$', RedirectView.as_view(url='login', permanent=False), name='index')
]
