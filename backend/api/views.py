from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from backend.spider.jdSpider import jdSpider, to_excel
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


# celery -A proj worker -l info -P eventlet
def test_index(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=jdK8STask.xls'
    result = jdSpider.delay()
    head_data, results = result.get(timeout=1000)
    to_excel(head_data, results).save(response)
    return response
