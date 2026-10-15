from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import(EventListCreate,EventDetail,RegisterView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('events/', EventListCreate.as_view(), name='events'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event'),
]