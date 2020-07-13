from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [

    path('', views.index, name='index'),
    path('<int:vote_id>/', views.detail, name='detail'),
    path('<int:vote_id>/results', views.results, name='results'),
    path('<int:vote_id>/vote_for_person', views.vote_for_person, name='vote_for_person')
]