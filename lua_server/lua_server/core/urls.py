from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .viewsets.user import UserViewSet
from .viewsets.post import PostViewSet

router = routers.SimpleRouter(trailing_slash=False)
api_schema_docs = get_swagger_view(title='Lua LMS API')

router.register('users', UserViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', api_schema_docs),
    path('documentation/', api_schema_docs),
]
