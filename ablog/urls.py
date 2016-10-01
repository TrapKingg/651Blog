from django.conf.urls import url
from . import views

#Create your urls here!
urlpatterns = [
    url(r'^$', views.post_list),
]