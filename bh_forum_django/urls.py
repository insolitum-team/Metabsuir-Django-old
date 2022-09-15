from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path('students/', include('django.contrib.auth.urls')),
    path('students/', include('students.urls')),
]
