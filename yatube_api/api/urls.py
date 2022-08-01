from django.urls import include, path
from rest_framework import routers

from .views import CommentsViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentsViewSet,
                   basename='comments')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
