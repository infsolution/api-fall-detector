from django.urls import path, include
from . import views

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
    path('position/', views.PositionEstateList.as_view(), name=views.PositionEstateList.name),
    path('position/<int:pk>/', views.PositionEstateDetail.as_view(), name=views.PositionEstateDetail.name),
]
