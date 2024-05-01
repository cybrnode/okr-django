

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import sub_categories

urlpatterns = [
    path('get_subcategories/<str:checklist>', sub_categories),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
