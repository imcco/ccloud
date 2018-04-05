from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^index/$', views.index, name='index'),
    url(r'^quite/$', views.quite, name='quite'),
    url(r'^user/$', views.user, name='user'),
    url(r'^useradd/$', views.useradd, name='useradd'),
    url(r'^usermod/$', views.usermod, name='usermod'),
    url(r'^userdel/$', views.userdel, name='userdel'),
    url(r'^usersave/$', views.usersave, name='usersave'),
    url(r'^image/$', views.image, name='image'),
    url(r'^imageadd/$', views.imageadd, name='imageadd'),
    url(r'^imagedel/$', views.imagedel, name='imagedel'),
    url(r'^imagesave/$', views.imagesave, name='imagesave'),
    url(r'^template/$', views.template, name='template'),
    url(r'^tempadd/$', views.tempadd, name='tempadd'),
    url(r'^tempdel/$', views.tempdel, name='tempdel'),
    url(r'^tempmod/$', views.tempmod, name='tempmod'),
    url(r'^tempsave/$', views.tempsave, name='tempsave'),
    url(r'^host/$', views.host, name='host'),
    url(r'^vmadd/$', views.vmadd, name='vmadd'),
    url(r'^vmdefine/$', views.vmdefine, name='vmdefine'),
    url(r'^host/vmopen/$', views.vmopen, name='vmopen'),
]