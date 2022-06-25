from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Flat
from django.urls import reverse

def index(request):
    flats_list = Flat.objects.order_by('-price')
    template = loader.get_template('wcity/index.html')
    context = {
        'flats_list': flats_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request, flat_id):
    flat = get_object_or_404(Flat, pk=flat_id)
    return render(request, 'wcity/detail.html', {'flat': flat})

def rent(request, flat_id):
    selected_flat = get_object_or_404(Flat, pk=flat_id)
    selected_flat.isRent = False
    selected_flat.save()
    return HttpResponseRedirect(reverse('wcity:index'))