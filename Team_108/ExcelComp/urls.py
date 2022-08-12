from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('library/', views.library, name="library"),
    path('libgrid/', views.libgrid, name="libgrid"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('featureselect/', views.featureselect, name="feature"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginPage, name="login"),
    path('terms/', views.terms, name="terms"),
    path('signup/', views.signup, name="signup"),
    path('singlefile/', views.singlefile, name="singlefile"),
    path('multifiles/', views.multifiles, name="multifiles"),
    path('contact/', views.contact, name="contact"),
    path('customer/', views.customer, name="customer"),
]
