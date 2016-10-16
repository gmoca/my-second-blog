from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', view = views.index_view, name='home'),
]