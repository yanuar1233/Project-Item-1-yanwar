from django.contrib import admin
from django.urls import path
from rest_framework import routers
from musicproject.views import views

routers = routers.DefaultRouter()
router.register('album', views.AlbumViewset)
router.register('song', views.SongViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musicproject/', include(router.urls)),
    path('musicproject-auth/', include('rest_framework', namespace='rest_framework'))
]
# yan
