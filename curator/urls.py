from django.urls import path

from . import views

app_name = 'curator'
urlpatterns = [
    path('', views.index, name='index'),
    path('curated', views.display_curated, name='curated'),
    path('word_type', views.word_type, name='word_type'),
    path('delete_first_base', views.delete_first_base, name='delete_first_base'),
]
