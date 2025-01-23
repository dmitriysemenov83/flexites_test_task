from rest_framework import serializers

from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):

    users = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'users']  # добавляем поле юзер
    @staticmethod
    def get_users(obj):
        users = obj.users.all() # Получаем пользователей, связанных с данной организацией
        return [
            {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            for user in users
        ]