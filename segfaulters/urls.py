from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from .views import home, profile, search
from django.urls import path,include

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^profile/$', profile,name='profile'),
    #url(r'^logoutt/$', views.LogoutView.as_view(template_name='registration/logout.html'), name='logoutt'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', home, name='home'),
    url(r'^search/$', search, name='search'),

    #listings app
    path('listings/',include('listings.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve,{
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
