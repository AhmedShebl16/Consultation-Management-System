from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import IndexView

urlpatterns = [
    # Frontend Entrypoint
    path('', IndexView.as_view(), name='index'),

    path('admin/', admin.site.urls),
    
    # API Endpoints
    path('api/', include('medical.urls')),
    
    # OpenAPI Schema (needed for Swagger UI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Swagger UI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
