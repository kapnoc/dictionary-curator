from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.forms import modelformset_factory
from django.core.paginator import Paginator

from .models import BaseEntry, CuratedEntry
from .forms import CuratedEntryForm, WordTypeForm


def curated(request):
    curated_formset = None
    CuratedEntryFormset = modelformset_factory(CuratedEntry, exclude=())
    if request.method == 'POST':
        curated_formset = CuratedEntryFormset(request.POST)
        if curated_formset.is_valid():
            curated_formset.save()
            return HttpResponseRedirect(reverse('curator:curated'))
        else:
            # go back to normal display, with errors in curated_display
            pass
    curated = CuratedEntry.objects.all().order_by('-pk')
    paginator = Paginator(curated, 5)
    page = request.GET.get('page', 1)
    if curated_formset is None:
        curated_formset = CuratedEntryFormset(
            queryset=paginator.page(page).object_list)
    context = {
        'curated': curated_formset,
        'page_range': paginator.page_range,
        'curr_page': int(page),
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
    curated_form = None
    if request.method == 'POST':
        form = CuratedEntryForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            # BaseEntry.objects.first().delete()
            return HttpResponseRedirect(reverse('curator:index'))
        else:
            curated_form = form
            # go back to normal display, with errors in curated_form
    base = BaseEntry.objects.first()
    if curated_form is None:
        curated_form = CuratedEntryForm()
    word_type_form = WordTypeForm()
    context = {
        'base': base,
        'curated_form': curated_form,
        'word_type_form': word_type_form,
    }
    return render(request, 'curate.html', context)
