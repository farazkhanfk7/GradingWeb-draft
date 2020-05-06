from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('addsub',views.addsub,name="addsub"),
    path('addmark',views.addmark,name="addmark"),
    path('addstud',views.addstud,name="addstud"),
    path('search',views.search,name="search")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)