from django.urls import path, include
from . import views

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
	path('user/', views.UserList.as_view(), name=views.UserList.name),
	path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
	path('device/', views.DeviceList.as_view(), name=views.DeviceList.name),
	path('device/<int:pk>/', views.DeviceDetail.as_view(), name=views.DeviceDetail.name),
    path('position/', views.PositionEstateList.as_view(), name=views.PositionEstateList.name),
    path('position/<int:pk>/', views.PositionEstateDetail.as_view(), name=views.PositionEstateDetail.name),
    path('dataset/', views.DataSetList.as_view(), name=views.DataSetList.name),
    path('dataset/<int:pk>/', views.DataSetDetail.as_view(), name=views.DataSetDetail.name),
]
