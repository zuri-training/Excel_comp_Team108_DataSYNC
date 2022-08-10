
# Register your models here.

from django.contrib import admin
from django.urls import path, include

# Register your models here.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls'))
]
