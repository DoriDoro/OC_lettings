from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from lettings.models import Letting


class LettingListView(ListView):
    model = Letting
    template_name = 'lettings_index.html'
    context_object_name = 'lettings_list'


class LettingDetailView(DetailView):
    model = Letting
    template_name = 'letting.html'

    def get_object(self, queryset=None):
        letting_id = self.kwargs.get('letting_id')
        return get_object_or_404(Letting, pk=letting_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['address'] = self.object.address
        return context
