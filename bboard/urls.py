from django.urls import path

from .views import index, hello, by_rubric
from .views import BbCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubrics'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('hello/', hello, name='hello'),
]
