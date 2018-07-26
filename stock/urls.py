from django.urls import path, include
from .views import *
	

urlpatterns = [
  #  url(r'^user/(?P<lotes>[-\w]+)/$', bookmark_user, name='stock_lotes_create'),
    # url(r'^create/$', lotes_create, name='stock_lotes_create'),
    # url(r'^edit/(?P<pk>\d+)/$', lotes_edit, name='stock_lotes_edit'),
    # url(r'^$', lotes_list, name='stock_lotes_list'),
    path('create/', lotes_create, name='stock_lotes_create'),
    path('edit/<int:pk>/', lotes_edit, name='stock_lotes_edit'),
    path('', lotes_list, name='stock_lotes_list'),
]