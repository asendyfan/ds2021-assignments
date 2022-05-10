"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from web_vault import views


urlpatterns = [
    path('', views.index),
    re_path(r'^(?P<id>exp\d+)$', views.project, name='project'),
    # re_path(r'^(?P<id>exp\d+)/patients', views.projectPatients),
    re_path(r'^(?P<id>exp\d+)/sessions$', views.projectSessions),
    re_path(r'^(?P<id>exp\d+)/(?P<sessionid>session\d+)$', views.stimulus),
    re_path(r'^(?P<id>exp\d+)/(?P<sessionid>session\d+)/(?P<stimulusid>sti\d+)$', views.endpoint),
    re_path(r'^(?P<id>exp\d+)/(?P<sessionid>session\d+)/(?P<stimulusid>sti\d+)/patient/(?P<type>\w+)', views.patient),
    re_path(r'^(?P<id>exp\d+)/(?P<sessionid>session\d+)/(?P<stimulusid>sti\d+)/method_(?P<endpointmethod>\w+)/type_(?P<endpointtype>\w+)$', views.endpointWithType),
    re_path(r'^(?P<id>exp\d+)/(?P<sessionid>session\d+)/(?P<stimulusid>sti\d+)/type_(?P<endpointtype>\w+)$', views.endpointWithType),
    re_path(r'^(?P<id>exp\d+)/(?P<sessionid>session\d+)/(?P<stimulusid>sti\d+)/download$', views.endpointDownload),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('reset/', views.reset, name='reset'),
    path('logout/', views.logout),
]


