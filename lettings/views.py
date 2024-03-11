from django.shortcuts import render

from lettings.models import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    single_letting = Letting.objects.get(id=letting_id)
    context = {
        'title': single_letting.title,
        'address': single_letting.address,
    }
    return render(request, 'letting.html', context)
