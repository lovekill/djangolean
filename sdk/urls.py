from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sdk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/',include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/',include('game.urls')),
]
