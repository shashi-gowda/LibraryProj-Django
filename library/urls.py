"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
    path('accounts/', include('django.contrib.auth.urls')) ##Look below for details
]

#instead of going to local host, there is a way to always redirect from local host to app
#it is from django.generic.views, see above to understand and see below for example

## www.example.com ===> example.com/app

#Note: '' ==> is representation of local host or domain page or Home age

''' IMP NOTE: adding django.contrib.auth.urls enales users to login, logout, 
password change and reset etc, this is from django source code'''

'''Note: djnago takes care of urls and views for accounts, but template should be created by djnago user, 
it is creted at site level in templates folder '''

'''NOTE: dont forget to add templates at site level using os.path.join '''