"""lua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from two_factor.urls import urlpatterns as tf_urls
# from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
# from two_factor.admin import AdminSiteOTPRequired
from django.conf import settings

# admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    # path('', include(tf_urls)),
    # path('', include(tf_twilio_urls)),
    path('admin/', admin.site.urls),

    # ...
    path('api/v1/', include('lua.core.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('nested_admin/', include('nested_admin.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
