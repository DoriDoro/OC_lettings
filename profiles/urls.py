from django.urls import path

from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.ProfileListView.as_view(), name='profiles_index'),
    path('profiles/<str:username>/', views.ProfileDetailView.as_view(), name='profile'),
]
