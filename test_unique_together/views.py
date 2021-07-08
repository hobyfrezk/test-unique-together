from rest_framework import viewsets
from rest_framework.response import Response

from .models import Tweet
from .serializers import TweetSerializer, TweetSerializerForCreate


class TweetViewSet(viewsets.GenericViewSet,
                   viewsets.mixins.CreateModelMixin
                   ):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()

    def get_permissions(self):
        return []

    def create(self, request, *args, **kwargs):
        serializer = TweetSerializerForCreate(
            data=request.data, context={"request": request}
        )

        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': 'Please check input.',
                'errors': serializer.errors,
            }, status=400)

        tweet = serializer.save()

        return Response({
            'success': True,
            'appointment': TweetSerializer(tweet).data
        }, status=201)
