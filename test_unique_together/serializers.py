from rest_framework import serializers
from test_unique_together.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'content', 'dummy_column')


class TweetSerializerForCreate(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'content', 'dummy_column')

    def create(self, validated_data):
        user = self.context['request'].user
        content = validated_data["content"]
        dummy_column = validated_data["dummy_column"]

        tweet = Tweet.objects.create(
            user=user, content=content, dummy_column=dummy_column
        )

        return tweet