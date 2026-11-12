from rest_framework import serializers
from app.models import employee

# class EmployeeSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     MODE_CHOICES =[('female','female'),('male','male')]
#     name=serializers.CharField(max_length=30)
#     empid=serializers.IntegerField()
#     age=serializers.IntegerField()
#     place=serializers.CharField(max_length=30)
#     gender=serializers.ChoiceField(choices=MODE_CHOICES)
#     joining_date=serializers.DateField(read_only=True)
#     salary=serializers.IntegerField()
#     designation=serializers.CharField(max_length=50)
#
#     def create(self, validated_data):
#         data = employee.objects.create(**validated_data)
#         return data
#
#     def update(self,instance,validated_data):
#         instance.empid= validated_data.get('empid',instance.empid)
#         instance.name= validated_data.get('name',  instance.name)
#         instance.age= validated_data.get('age', instance.age)
#         instance.place= validated_data.get('place',instance.place)
#         instance.gender= validated_data.get('gender',instance.gender)
#         instance.salary= validated_data.get('salary',instance.salary)
#         instance.designation= validated_data.get('designation',instance.designation)
#         instance.save()
#         return instance



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:

        model = employee
        fields = '__all__'
        read_only_field = ['id','joining_date']
