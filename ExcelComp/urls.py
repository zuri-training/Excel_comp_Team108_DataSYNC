from django.urls import path
from django.conf import urls
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
    path('aboutus/', views.aboutus, name="aboutus"),
    path('faq/', views.faq, name="faq"),
    path('mission/', views.mission, name="mission"),
    path('convert/', views.convert, name="convert"),
    # path('multipleupload/', views.multipleupload, name="multipleupload"),

]

handler404 = 'ExcelComp.views.error_404'
handler500 = 'ExcelComp.views.error_500'
handler403 = 'ExcelComp.views.error_403'
handler400 = 'ExcelComp.views.error_400'
