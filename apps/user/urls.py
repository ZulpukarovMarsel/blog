from django.urls import path, include
from .views import SignUpAPIView, SignInAPIView, LogoutAPIView, NotificationListCreateAPIView, NotificationRetrieveDestroyAPIView, index

urlpatterns = [
    path('sign_up/', SignUpAPIView.as_view(), name='sign_up'),
    path('sign_in/', SignInAPIView.as_view(), name='sign_in'),
    path('sign_out/', LogoutAPIView.as_view(), name='sign_out'),
    path('notifications/', NotificationListCreateAPIView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationRetrieveDestroyAPIView.as_view(), name='notification-retrieve-destroy'),
    path('', index, name='home'),
]