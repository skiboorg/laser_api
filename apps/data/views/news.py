from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from apps.data.serializers.news import *
from apps.data.serializers.service import TeamSerializer
from apps.data.models.cb import CallbackForm,Team

class GetNews(generics.ListAPIView):
    serializer_class = NewsItemShortSerializer
    def get_queryset(self):
        for_index_param = self.request.GET.get('index', None)
        for_index = True if for_index_param.lower() == 'true' else False
        if for_index:
            queryset = NewsItem.objects.filter(show_on_main=True)
        else:
            queryset = NewsItem.objects.all()
        return queryset


class GetNewsItem(generics.RetrieveAPIView):
    serializer_class = NewsItemSerializer
    queryset = NewsItem.objects.filter()
    lookup_field = 'slug'


class NewForm(generics.CreateAPIView):
    queryset = CallbackForm
    serializer_class = CallbackFormSerializer
    parser_classes = [MultiPartParser, FormParser]

class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
