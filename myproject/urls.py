from django.contrib import admin
from django.urls import path, include  # імпортуємо include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Додаємо URL-адреси з myapp
]
