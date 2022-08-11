from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.contact, name="about"),
    path('customer/', views.customer, name="customer"),
    path('library/', views.library, name="library"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('multifiles/', views.multifiles, name="multifiles"),
    path('signup/', views.signup, name="signup"),
    path('singlefile/', views.singlefile, name="singlefile"),
    path('terms/', views.terms, name="terms"),
]
