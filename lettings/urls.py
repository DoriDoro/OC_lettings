from django.urls import path

from lettings import views

app_name = 'lettings'

urlpatterns = [
    path('lettings/', views.LettingListView.as_view(), name='lettings_index'),
    path('lettings/<int:letting_id>/', views.LettingDetailView.as_view(), name='letting'),
]
