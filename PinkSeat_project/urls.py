from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/account/', include(('restaccount_app.urls', 'restprofile'), namespace='restaccount')),
]
