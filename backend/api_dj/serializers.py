from rest_framework import serializers

from posts_views.models import Images
from posts_views.url_validators import check_correctness_url
from posts_views.utils import get_image_from_url


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = (
            "id", "name", "url", "picture",
            "width", "height", "parent_picture"
        )

    def validate_url(self, data):
        url = self.initial_data.get("url")
        check_correctness_url(url)
        return data

    def create(self, validated_data):
        url = validated_data.get("url")
        if url:
            picture = get_image_from_url(url)
            validated_data["picture"] = picture
        return Images.objects.create(**validated_data)
