from django.shortcuts import render

from oc_lettings_site.models import Profile  # TODO: change after migration


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    single_profile = Profile.objects.get(user__username=username)
    context = {'profile': single_profile}
    return render(request, 'profile.html', context)
