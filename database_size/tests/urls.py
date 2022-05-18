from django.urls import re_path, include

from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', include(admin.site.urls)),
]
