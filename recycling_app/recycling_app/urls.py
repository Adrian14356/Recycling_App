from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("core.urls")),
    path("", include("users.urls")),
    path('bin-type/', include('bin_type_rest_api.urls'))
]
