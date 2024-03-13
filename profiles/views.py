from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from profiles.models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles_index.html'
    # overwrites, otherwise: templates/app_name/profile_list.html
    context_object_name = 'profiles_list'  # renames the context_name, otherwise: profile_list


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(Profile, user__username=username)

