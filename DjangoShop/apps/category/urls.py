from django.conf.urls import include, url
from category import api

app_name = 'category'

urlpatterns = [
    url(r'^all/','views.CategoryCollection',name='CategoryCollection'),
    url(r'^see/(?P<id>\d+)','views.SingleCategory',name='SingleCategory'),

    #REST URLS
    url(r'', api.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', api.CategoryDetail.as_view()),
]