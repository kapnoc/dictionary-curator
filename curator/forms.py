from django import forms

from .models import WordType, CuratedEntry


class WordTypeForm(forms.ModelForm):
    class Meta:
        model = WordType
        fields = ['name']


class CuratedEntryForm(forms.ModelForm):
    class Meta:
        model = CuratedEntry
        fields = ['version', 'fr', 'vo', 'gender',
                  'multiple_words', 'notes', 'word_type']
