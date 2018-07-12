from rest_framework.test import APITestCase
from django.urls import reverse
from kakao_auto_reply.response import (
    MessageResponse, Message, Keyboard, Photo, MessageButton
)


class TestKakaoAutoReplyAPITest(APITestCase):
    def test_on_keyboard_api(self):
        """
        Request GET /keyboard
        Response 200 { "type": "buttons", "buttons": ["foo", "bar"] }
        """

        response = self.client.get(reverse('test-on_keyboard'), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['type'], 'buttons')
        self.assertListEqual(response.data['buttons'], ['foo', 'bar'])

    def test_on_message_api(self):
        """
        Request POST /message
        Response 200 { "message": { "text": "echo: foo" } }
        """

        data = {'type': 'text', 'content': 'foo', 'user_key': 'test_user_key'}
        response = self.client.post(reverse('test-on_message'), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, {'message': {'text': 'echo: foo'}})

    def test_on_friend_added(self):
        """
        Request POST /friend
        Response 204
        """

        data = {'user_key': 'test_user_key'}
        response = self.client.post(reverse('test-on_friend_added'), data, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

    def test_on_friend_deleted(self):
        """
        Request DELETE /friend/test_user_key
        Response 204
        """

        response = self.client.delete(reverse('test-on_friend_deleted', kwargs={'pk': 'test_user_key'}), format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

    def test_on_chatroom_leaved(self):
        """
        Request DELETE /friend/test_user_key
        Response 204
        """

        response = self.client.delete(reverse('test-on_chatroom_leaved', kwargs={'pk': 'test_user_key'}), format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

    def test_not_provided(self):
        data = {'type': 'text', 'content': 'foo', 'user_key': 'test_user_key'}

        response = self.client.get(reverse('not_provided_test-on_keyboard'),
                                   format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

        response = self.client.post(reverse('not_provided_test-on_friend_added'),
                                    data, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

        response = self.client.post(reverse('not_provided_test-on_friend_added'),
                                    data, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

        response = self.client.delete(reverse('not_provided_test-on_friend_deleted', kwargs={'pk': 'test_user_key'}),
                                      format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)

        response = self.client.delete(reverse('not_provided_test-on_chatroom_leaved', kwargs={'pk': 'test_user_key'}),
                                      format='json')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(response.data)


class TestKakaoAutoReplyResponseTest(APITestCase):
    def test_message_response_assertion_error_if_message_is_none(self):
        with self.assertRaises(AssertionError) as context:
            MessageResponse(message=None)
        self.assertTrue(context)

    def test_keyboard_assertion_error_if_type_is_not_allowed(self):
        with self.assertRaises(AssertionError) as context:
            Keyboard(type='foo')
        self.assertTrue(context)

    def test_photo_assertion_error_if_none_in_args(self):
        with self.assertRaises(AssertionError) as context1:
            Photo(None, 'foo', 'bar')

        with self.assertRaises(AssertionError) as context2:
            Photo('foo', None, 'bar')

        with self.assertRaises(AssertionError) as context3:
            Photo('foo', 'bar', None)

        self.assertTrue(context1)
        self.assertTrue(context2)
        self.assertTrue(context3)

    def test_message_button_assertion_error_if_none_in_args(self):
        with self.assertRaises(AssertionError) as context1:
            MessageButton(None, 'foo')

        with self.assertRaises(AssertionError) as context2:
            MessageButton('foo', None)

        self.assertTrue(context1)
        self.assertTrue(context2)

    def test_message_response(self):
        photo = Photo(url='foo', width=100, height=100)
        message_button = MessageButton(url='bar', label='zoo')
        message = Message(text='foo', photo=photo, message_button=message_button)
        keyboard = Keyboard(type='text')
        data = MessageResponse(message, keyboard)
        self.assertDictEqual(data['message'], message)
        self.assertDictEqual(data['keyboard'], keyboard)
