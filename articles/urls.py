from unicodedata import name
from django.urls import path 
from . import views
app_name = 'articles'

urlpatterns=[
    path('',views.home,name='home'),
    path('article/<int:id>/',views.article,name="article"),
    path('search/',views.search,name='search'),
    path('create/',views.article_create,name='create')
]