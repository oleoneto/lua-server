from rest_framework import serializers
from ..models.assignment import Assignment, Question, Option
from ..models.assignment import AssignmentFile, FileSubmission, AssignmentType


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, allow_null=True)

    class Meta:
        model = Question
        fields = "__all__"


class AssignmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentType
        fields = ('id', 'description')


class AssignmentSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, allow_null=True)
    assignment_type = AssignmentTypeSerializer()

    class Meta:
        model = Assignment
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['assignment_type', 'questions']
