"""webplayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from pages.urls import pages_patterns
from profiles.urls import profile_patterns
from messenger.urls import messenger_patterns
from django.conf import settings
# from jet_django.urls import jet_urls
#from django.conf.urls import url


urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
 #   url(r'^jet/', include(('jet.urls', 'jet'))),
   # url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
    # Paths de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profile_patterns)),
    # Paths de messenger
    path('messenger/', include(messenger_patterns)),
   # url(r'^jet_api/', include(jet_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
