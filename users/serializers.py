from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()  # получаем организации

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'avatar', 'organizations')

    @staticmethod
    def get_organizations(obj):

        return [
            {
                'id': org.id,
                'name': org.name,
                'description': org.description,
            }
            for org in obj.organizations.all()
        ]
