from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$',views.home,name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^content/$', views.post_list, name='content'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^sign_up/$', views.signup, name='signup'),
    url(r'^sign_in/$', views.signin, name='signin'),
    url(r'^log_out/$', views.log_out, name='log_out'),
]   
