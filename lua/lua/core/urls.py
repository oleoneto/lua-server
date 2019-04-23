from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views
from .viewsets import router

api_schema_docs = get_swagger_view(title='Lua LMS API')

urlpatterns = [
    # REST API Endpoints
    path('', include(router.urls)),

    # Documentation
    path('documentation/', api_schema_docs),

    # Authentication
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
