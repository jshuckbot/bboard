from rest_framework import serializers

from main.models import Bb, Comment


class BbSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ("id", "title", "content", "price", "created_at")


class BbDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ("id", "title", "content", "price", "created_at", "contacts", "image")


class CommentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "bb",
            "author",
            "content",
            "created_at",
        )
