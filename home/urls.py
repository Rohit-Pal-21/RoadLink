from django.urls import path
from . import views
app_name='home'
urlpatterns = [
	path('404', views.notfound,name='404'),
    path('', views.index,name='index'),
]