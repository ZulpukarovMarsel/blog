from django.urls import path, include
from .views import BlogViewSet, TagsViewSet, CommentViewSet, LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tags', TagsViewSet),
router.register(r'comment', CommentViewSet),
router.register(r'like', LikeViewSet),
router.register(r'blog', BlogViewSet),


urlpatterns = [
    path('api/', include(router.urls)),
]