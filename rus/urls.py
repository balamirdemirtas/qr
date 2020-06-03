from django.urls import path
from . import views




app = 'rus'


urlpatterns =[
    path('rusindex/',views.rusindex,name='engindex'),
    path('<str:category_slug>/',views.russhow,name='russhow_category'),

]