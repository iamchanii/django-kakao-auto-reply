from rest_framework.response import Response
from kakao_auto_reply import decorators
from kakao_auto_reply.objects import MessageResponse, Message, Keyboard
from kakao_auto_reply.viewsets import KakaoAutoReplyViewSet


class TestNotProvidedKakaoAutoReplyViewSet(KakaoAutoReplyViewSet):
    pass


class TestKakaoAutoReplyViewSet(KakaoAutoReplyViewSet):
    def on_keyboard(self, request, *args, **kwargs):
        data = Keyboard(type='buttons', buttons=['foo', 'bar'])
        return Response(data, 200)

    @decorators.on_message_parse
    def on_message(self, request, *args, **kwargs):
        content = kwargs['content']

        text = 'echo: %s' % content
        message = Message(text=text)
        data = MessageResponse(message=message)
        return Response(data, 200)

    @decorators.on_friend_added_parse
    def on_friend_added(self, request, *args, **kwargs):
        user_key = kwargs['user_key']

        print('on_friend_added: %s' % user_key)
        return Response(None, 204)

    @decorators.on_friend_deleted_parse
    def on_friend_deleted(self, request, *args, **kwargs):
        user_key = kwargs['user_key']

        print('on_friend_deleted: %s' % user_key)
        return Response(None, 204)

    @decorators.on_chatroom_leaved_parse
    def on_chatroom_leaved(self, request, *args, **kwargs):
        user_key = kwargs['user_key']

        print('on_chatroom_leaved: %s' % user_key)
        return Response(None, 204)
