from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from .views import home, profile
from django.urls import path,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='home.html'), name='logout'),
    url(r'^profile/$', profile,name='profile'),
    #url(r'^logoutt/$', views.LogoutView.as_view(template_name='registration/logout.html'), name='logoutt'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', home, name='home'),

    #listings app
    path('listings/',include('listings.urls')),
]
