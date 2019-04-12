from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from .views import *
from .viewsets import router

api_schema_docs = get_swagger_view(title='Lua LMS API')

urlpatterns = [
    # REST API Endpoints
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/docs/', api_schema_docs),
    path('api/v1/documentation/', api_schema_docs),

    # TODO: Implement templates
    # path('accounts/', include('django_registration.backends.activation.urls')),

    # Pages
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('documentation/', DocumentationView.as_view(), name='documentation'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
