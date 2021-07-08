"""models.py"""
class Tweet(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255)
    dummy_column = models.CharField(max_length=255)

    # class Meta:
    #     unique_together = (
    #         ('user', 'dummy_column'),
    #     )

"""serializers.py"""
class TweetSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'content', 'dummy_column')

    def create(self, validated_data):
        user = self.context['request'].user
        content = validated_data["content"]
        dummy_column = validated_data["dummy_column"]
        tweet = Tweet.objects.create(user=user, content=content, dummy_column=dummy_column)
        return tweet

"""views.py"""
class TweetViewSet(viewsets.GenericViewSet,viewsets.mixins.CreateModelMixin):

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
