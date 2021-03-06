"""FarmHelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('app.urls')),
    url(r'^farmerid/(?P<pk>[0-9]+)/$', views.FarmerDetail),
    url(r'^farmer/',views.FarmerList.as_view()),
    url(r'^memberid/(?P<pk>[0-9]+)/$', views.MemberDetail),
    url(r'^member/',views.MemberList.as_view()),
    url(r'^householdid/(?P<pk>[0-9]+)/$', views.HouseHoldDetail),
    url(r'^household/', views.HouseHoldList.as_view()),
    url(r'^maps/', views.maps),
    url(r'^maplist/', views.MapList.as_view()),
    url(r'^maplistid/(?P<pk>[0-9]+)/$', views.MapDetail),
    url(r'^farms/',views.FarmList.as_view()),
#    url(r'^farmdet/',views.News.as_view()),
    url(r'^wells/', views.Wells.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)
