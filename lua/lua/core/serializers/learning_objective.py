from rest_framework import serializers
from django.core.exceptions import ValidationError
from ..models.learning_objective import LearningObjective, LearningOutcome
from ..models.learning_objective import LearningObjectiveFile, LearningLevel


class LearningLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningLevel
        fields = "__all__"


class LearningOutcomeSerializer(serializers.ModelSerializer):
    learning_levels = LearningLevelSerializer(many=True, allow_null=True)

    class Meta:
        model = LearningOutcome
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['learning_levels']


class LearningObjectiveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningObjectiveFile
        fields = "__all__"


class LearningObjectiveSerializer(serializers.ModelSerializer):
    outcomes = LearningOutcomeSerializer(many=True, allow_null=True)
    files = LearningObjectiveFileSerializer(many=True, allow_null=True)

    class Meta:
        model = LearningObjective
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['outcomes', 'files']

    # TODO: Test implementation
    def create(self, validated_data):
        outcomes = validated_data.pop('outcomes')
        files = validated_data.pop('files')
        try:
            instance = LearningOutcome.objects.create(**validated_data)
            for outcome in outcomes:
                instance.outcomes.add(outcome)
        except ValidationError as e:
            raise serializers.ValidationError(e.args[0])



        return instance

    def update(self, instance, validated_data):
        instance.save()
        return instance
