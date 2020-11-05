from django.db import models


class BaseEntry(models.Model):
    fr = models.TextField()
    vo = models.TextField()

    class Meta:
        db_table = 'defs'


class WordType(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'word_types'


GENDER_CHOICES = [
    ('N', 'Neutre'),
    ('F', 'Féminin'),
    ('M', 'Masculin'),
]


class CuratedEntry(models.Model):
    version = models.PositiveIntegerField(default=1)
    fr = models.TextField()
    vo = models.TextField()
    notes = models.TextField(blank=True, default="")
    multiple_words = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='N',
    )
    word_type = models.ForeignKey(WordType, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'entries'
