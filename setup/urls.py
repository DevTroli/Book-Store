from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import update

# Configuração do Swagger/OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Book-Store API",
        default_version='v1',
        description="API para gerenciamento de livraria",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Configuração das URLs
urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=False), name='root'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api_token-auth/", obtain_auth_token, name="api_token-auth"),
    path("update_server/", update, name="update"),
]
