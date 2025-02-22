from django.contrib import admin
from django.urls import path, include
import lettings.urls
import profiles.urls
from oc_lettings_site.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lettings/', include(lettings.urls)),
    path('profiles/', include(profiles.urls)),
]
