from django.urls import path

from core.views import index

app_name = 'core'

handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'

urlpatterns = [
    path('', index, name='index'),
]
