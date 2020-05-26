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
    path('profile/<int:pk>', views.ShowProfile.as_view(), name='profile'),
    path('modifica/<int:pk>', views.ModifyUser.as_view(), name='modificauser'),
    path('modificaPassword', views.PasswordChangeView, name='modica-password'),
    path('deleteText', views.DeleteText.as_view(), name='delete-text'),
    path('addText', views.add_text, name='add-text'),
    path('addText/check',  views.check_text_is_unique, name='check-text-unique'),
    path('homepage', views.Homepage, name='homepage'),
    path('analyzeAllWords', views.allwords, name='analyze-all-words'),
    path('analyzeAllPersonalWords', views.allPersonalWords, name='analyze-all-personal-words'),
    path('search', views.search_titles, name='search'),
    path('features/<int:pk>', views.featuresText, name='features-text'),
    path('blacklist', views.blacklist, name='blacklist'),
    path('blacklist/delete',  views.DeleteBlacklist.as_view(), name='delete-blacklist'),
    path('graph/<int:pk>',  views.graphSingleText, name='graph'),
    path('graphPersonalText',  views.graphPersonalText, name='graph-personal-text'),
    path('graphAllText',  views.graphAllText, name='graph-all-text'),
    path('blacklist/return',  views.returnBlacklist, name='return-blacklist'),
    path('select',  views.select_for_compare, name='select-text'),
    path('compare/<int:key_testi1>/<int:key_testi2>',  views.compare_text, name='compare-text'),
    re_path(r'^$', RedirectView.as_view(url='login', permanent=False), name='index')
]
