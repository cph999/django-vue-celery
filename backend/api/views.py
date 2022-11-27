from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from backend.demoapp.tasks import add
from .models import Message, MessageSerializer, UserInfo, UserInfoSerializer
from celery.result import AsyncResult

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


def test_index(request):
    result = add.delay(255, 327)
    res = result.get(timeout=1)
    return HttpResponse(result.id + "    " + str(res))
