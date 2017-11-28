from django.conf.urls import url
from views import register, login, new, users, register


urlpatterns = [
    url(r'^$', register),
    url(r'^login', login),
    url(r'^new', new),
    url(r'^users', users),
    url(r'^register', register),


]