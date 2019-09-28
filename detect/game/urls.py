from django.urls import path, include
from . import views

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
	path('user/', views.UserList.as_view(), name=views.UserList.name),
	path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
]
