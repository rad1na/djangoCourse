from django.contrib import admin
from django.urls import path
import debug_toolbar
from django.conf import settings
from django.urls import include, path
from cms import urls as cms_urls

urlpatterns = [
    path('', include(cms_urls)),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
