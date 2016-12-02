from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.index_view, name='home'),
    url(r'^about/$', view=views.AboutView.as_view(), name='about'),
    url(r'^contact/$', view=views.ContactView.as_view(), name='contact'),
]