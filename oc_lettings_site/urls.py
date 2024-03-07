from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('', include('lettings.urls', namespace='lettings')),
    path('', include('profiles.urls', namespace='profiles')),
]
