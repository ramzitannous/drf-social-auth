from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('api/', include('drf_social.urls')),
    re_path(r'^admin/?', admin.site.urls),
]