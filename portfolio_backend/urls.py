from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    # system
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # endpoints
    path("api/v1/health/", views.health, name="health"),
    path("api/v1/about/", include("about.urls", namespace="about"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = "Portfolio | Admin"
admin.site.site_header = "Portfolio | Admin"
admin.site.site_url = settings.FRONTEND_URL