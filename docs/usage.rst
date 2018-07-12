=====
Usage
=====

To use django-rest-kakao-auto-reply in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'kakao_auto_reply.apps.KakaoAutoReplyConfig',
        ...
    )

Add django-rest-kakao-auto-reply's URL patterns:

.. code-block:: python

    from kakao_auto_reply import urls as kakao_auto_reply_urls


    urlpatterns = [
        ...
        url(r'^', include(kakao_auto_reply_urls)),
        ...
    ]
