from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('' , views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup' ),
    path('logout/', views.logout, name = 'logout' ),
    path('profile/', views.profile, name = 'profile' ),
    
    # api config
    
    path('api/updateprofile/', views.updateprofile, name = 'updateprofile'),
    path('api/register/', views.register, name = 'register'),
    path('api/signin/', views.signin, name = 'signin')
]

urlpatterns += staticfiles_urlpatterns()