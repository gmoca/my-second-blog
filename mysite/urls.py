from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', include('home.urls')),
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),

]


if settings.DEBUG:
    urlpatterns.append(
        url(
            regex=r'^media/(?P<path>.*)$',
            view='django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}
        )
    )