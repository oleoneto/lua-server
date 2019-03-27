from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .viewsets.user import UserViewSet
from .viewsets.post import PostViewSet
from .views.index import IndexView
from .views.documentation import DocumentationView
from .views.faq import FAQView
from .views.pricing import PricingView
from .views.about import AboutView

router = routers.SimpleRouter(trailing_slash=False)
api_schema_docs = get_swagger_view(title='Lua LMS API')

router.register('users', UserViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    # REST API Endpoints
    path('api/v1/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', api_schema_docs),
    path('api/documentation/', api_schema_docs),

    # Pages
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('documentation', DocumentationView.as_view(), name='documentation'),
    path('faq', FAQView.as_view(), name='faq'),
    path('pricing', PricingView.as_view(), name='pricing'),
]
