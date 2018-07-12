from django.conf.urls import url, include
from kakao_auto_reply.routers import KakaoAutoReplyRouter
from .views import TestKakaoAutoReplyViewSet, TestNotProvidedKakaoAutoReplyViewSet

router = KakaoAutoReplyRouter()
router.register('', TestKakaoAutoReplyViewSet, base_name='test')

not_provided_router = KakaoAutoReplyRouter()
not_provided_router.register('', TestNotProvidedKakaoAutoReplyViewSet, base_name='not_provided_test')

urlpatterns = [
    url('', include(router.urls)),
    url('not_provided/', include(not_provided_router.urls)),
]
