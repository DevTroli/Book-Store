from bookstore import views
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Book-Store API",
        default_version='v1',
        description="API para gerenciamento de livraria",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', RedirectView.as_view(url='/swagger/', permanent=False), name='root'),
    # Documentação Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Admin do Django
    path("admin/", admin.site.urls),
    # Rotas versionadas
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    # Autenticação por token
    path("api_token-auth/", obtain_auth_token, name="api_token-auth"),
    # Atualização server automatica
    path("update_server/", views.update, name="update"),
]
