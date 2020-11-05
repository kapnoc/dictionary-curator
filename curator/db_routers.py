from .models import BaseEntry, WordType, CuratedEntry


class DictionaryRouter:

    def db_for_read(self, model, **hints):
        if model == BaseEntry:
            return 'base_dictionary'
        if model in [WordType, CuratedEntry]:
            return 'curated_dictionary'
        return None

    def db_for_write(self, model, **hints):
        if model == BaseEntry:
            return 'base_dictionary'
        if model in [WordType, CuratedEntry]:
            return 'curated_dictionary'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in ['WordType', 'CuratedEntry']:
            return db == 'curated_dictionary'
        return None
