from api import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


api_patterns = [
    path("appointment/", views.add_appointment),
    path("show/", views.show_appointments)
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_patterns)),
    
]
