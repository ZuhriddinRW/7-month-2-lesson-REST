from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from django_app.views import *

schema_view = get_schema_view (
    openapi.Info (
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact ( email="contact@snippets.local" ),
        license=openapi.License ( name="BSD License" ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path ( 'admin/', admin.site.urls ),

    path ( 'customers/', CustomerAPI.as_view (), name='customer-list' ),
    path ( 'customers/<slug:slug>/', CustomerDetailAPI.as_view (), name='customer-detail' ),

    path ( 'employees/', EmployeeAPI.as_view (), name='employee-list' ),
    path ( 'employees/<slug:slug>/', EmployeeDetailAPI.as_view (), name='employee-detail' ),

    path ( 'orders/', OrderAPI.as_view (), name='order-list' ),
    path ( 'orders/<slug:slug>/', OrderDetailAPI.as_view (), name='order-detail' ),

    path ( 'swagger<format>/', schema_view.without_ui ( cache_timeout=0 ), name='schema-json' ),
    path ( 'swagger/', schema_view.with_ui ( 'swagger', cache_timeout=0 ), name='schema-swagger-ui' ),
    path ( 'redoc/', schema_view.with_ui ( 'redoc', cache_timeout=0 ), name='schema-redoc' ),
]
