from django.urls import path
from . import views


#ana urlle direk atadık.

app = 'menu'


urlpatterns =[
    path('',views.index,name ='index'),
    path('<str:category_slug>/',views.show,name='show_category'),

]