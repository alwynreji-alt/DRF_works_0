from rest_framework import serializers
from app.models import movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:

        model = movie
        fields = '__all__'
        read_only_field = ['id','joining_date']
