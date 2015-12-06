from django.conf.urls import include, url

app_name = 'category'

urlpatterns = [
    url(r'^all/','views.CategoryCollection',name='CategoryCollection'),
    url(r'^see/(?P<id>\d+)','views.SingleCategory',name='SingleCategory'),
]