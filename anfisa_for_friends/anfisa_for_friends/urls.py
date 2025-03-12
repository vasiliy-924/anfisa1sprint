from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('homepage.urls', 'homepage'), namespace='homepage')),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('ice_cream/', include(('ice_cream.urls', 'ice_cream'), namespace='ice_cream')),
    path('admin/', admin.site.urls),
]
