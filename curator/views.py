from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import BaseEntry, CuratedEntry
from .forms import CuratedEntryForm, WordTypeForm


def display_curated(request):
    curated = CuratedEntry.objects.all()[:]
    print(curated)
    context = {
        'curated': curated,
    }
    return render(request, 'display_curated.html', context)


def delete_first_base(request):
    if request.method == 'POST':
        BaseEntry.objects.first().delete()
        return HttpResponseRedirect(reverse('curator:index'))


def word_type(request):
    if request.method == 'POST':
        form = WordTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('curator:index'))


def index(request):
    if request.method == 'POST':
        form = CuratedEntryForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            # BaseEntry.objects.first().delete()
            return HttpResponseRedirect(reverse('curator:index'))
        else:
            base = BaseEntry.objects.first()
            curated_form = form
            word_type_form = WordTypeForm()
            context = {
                'base': base,
                'curated_form': curated_form,
                'word_type_form': word_type_form,
            }
            return render(request, 'curate.html', context)

    base = BaseEntry.objects.first()
    curated_form = CuratedEntryForm()
    word_type_form = WordTypeForm()
    context = {
        'base': base,
        'curated_form': curated_form,
        'word_type_form': word_type_form,
    }
    return render(request, 'curate.html', context)
