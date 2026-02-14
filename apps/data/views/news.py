from rest_framework import generics
from apps.data.serializers.news import *

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