from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^codetester/', include('codetester.urls')),
    url(r'^admin/', admin.site.urls),
]