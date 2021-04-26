from django.urls import include, path
from rest_framework import routers
from . import views




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/hero/',views.get_post_hero,name='get_post_hero'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
