from django.http import Http404
from django.shortcuts import render

from lettings.models import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    # customize the error messages in DEBUG=True mode:
    try:
        single_letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        raise Http404(f'This Letting with id: {letting_id} does not exist!')
    context = {
        'title': single_letting.title,
        'address': single_letting.address,
    }
    return render(request, 'letting.html', context)
