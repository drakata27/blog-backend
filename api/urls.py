from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.get_routes, name="routes"),
    path('blogs/', views.get_blogs, name="blogs"),
    path('blogs/<str:pk>/', views.get_blog, name="blog"),
    path('blogs/<str:pk>/edit', views.update_blog, name="update-blog"),

    # Auth
    path('token/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('test/', views.test_endpoint, name='test'),
]