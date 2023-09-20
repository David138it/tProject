from django.conf.urls.static import static
from django.contrib import admin
from tapp import settings
from django.urls import path, include
from products.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound