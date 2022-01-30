from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from astro import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('about', views.about, name='about'), 
    path('addevent', views.addevent, name='addevent'), 
    path('showevent', views.showevent, name='showevent'),
    path('event<int:eid>', views.eventDetail, name='eventDetail'),

]
