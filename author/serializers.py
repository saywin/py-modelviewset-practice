from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
    # id = serializers.IntegerField(read_only=True)
    # first_name = serializers.CharField(max_length=64)
    # last_name = serializers.CharField(max_length=64)
    # pseudonym = serializers.CharField(max_length=64, required=False)
    # age = serializers.IntegerField()
    # retired = serializers.BooleanField()
    #
    # def create(self, validated_data):
    #     return Author.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get(
    #         "first_name",
    #         instance.first_name
    #     )
    #     instance.last_name = validated_data.get(
    #         "last_name",
    #         instance.last_name
    #     )
    #     instance.pseudonym = validated_data.get(
    #         "pseudonym",
    #         instance.pseudonym
    #     )
    #     instance.age = validated_data("age", instance.age)
    #     instance.retired = validated_data("retired", instance.pseudonym)
    #     instance.save()
    #     return instance
