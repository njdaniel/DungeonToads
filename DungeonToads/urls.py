"""DungeonToads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from toadapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^combat/', views.combat, name='combat'),
    url(r'^fight/(?P<id>\d+)', views.fight, name='fight'),
    url(r'^create_character/$', views.create_character, name='create_character'),
    url(r'^character_list/$', views.character_list, name='character_list'),
    url(r'^admin/', admin.site.urls),
    url(r'^character_detail/(?P<id>\d+)/', views.character_detail, name='character_detail')
]
