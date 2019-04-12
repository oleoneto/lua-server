from rest_framework import serializers


class ChoicesSerializerField(serializers.SerializerMethodField):
    """
    A read-only field that return the representation of a model field with choices.
    """

    def to_representation(self, value):
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        method = getattr(value, method_name)
        return method()
