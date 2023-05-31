from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # user manager
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    # local applications
    path('', include('pages.urls')),
    # path('accounts/', include('accounts.urls')),
]
