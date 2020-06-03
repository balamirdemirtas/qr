from django.urls import path
from . import views




app = 'eng'


urlpatterns =[
    path('engindex/',views.engindex,name='engindex'),
    path('<str:category_slug>/',views.engshow,name='engshow_category'),

]