from django.conf.urls import url, include
from django.views.generic import TemplateView

from mysite.books import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^routers/$', views.router_list, name='book_list'),
    url(r'^routers/create/$', views.router_create, name='book_create'),
    url(r'^routers/(?P<pk>\d+)/update/$', views.router_update, name='book_update'),
    url(r'^routers/(?P<pk>\d+)/delete/$', views.router_delete, name='book_delete'),
]
