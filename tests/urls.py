from django.conf.urls import url, include
from kakao_auto_reply.routers import KakaoAutoReplyRouter
from .views import TestKakaoAutoReplyViewSet

router = KakaoAutoReplyRouter()
router.register('', TestKakaoAutoReplyViewSet, base_name='test')

urlpatterns = [
    url('', include(router.urls)),
]
