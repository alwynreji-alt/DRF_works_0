
from django.contrib.sites import requests
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from appp.models import student,course


# Create your views here.

class studentlist(View):
    def get(self,response):
        data=[

            {'name': 'Alwyn',
             'Age': '21',
            'course': 'CSE',
            'mark': '80',},

            { 'name': 'Arun',
              'Age': '22',
            'course': 'CSE',
            'mark': '70',},

            {'name': 'Ravi',
             'Age': '23',
            'course': 'EEE',
            'mark': '70',}
        ]
        s=list(student.objects.all().values())
        print(s)
        return JsonResponse(s,safe=False)






class studentdetails(View):
    def get(self,response,i):
        s=student.objects.filter(id=1)
        print(s)
        data=list(s.values())
        print(data)


        return JsonResponse({"message": "success"})







#> CREATE (POST) <
from json import loads
from django.views.decorators.csrf import csrf_exempt
@method_decorator(csrf_exempt,name="dispatch")
class studentcreate(View):
    def post(self,request):
        form_data=request.body #json data


        data=loads(form_data)
        print(data)
        n=data['name']
        a=data['age']
        c = data['course']
        m=data['mark']


        s=student.objects.create(name=n,age=a,course=c,mark=m)
        s.save()
        return JsonResponse({"message":"created"})



# > DELETE <

@method_decorator(csrf_exempt, name="dispatch")
class studentdelete(View):
    def delete(self,request,i):
        s=student.objects.get(id=i)
        s.delete()
        return JsonResponse({"message":"Deleted"})


#> UPDATE FULL (PUT)<

@method_decorator(csrf_exempt, name="dispatch")
class studentupdate(View):
     def put(self,request,i):
         form_data=request.body
         data=loads(form_data)
         s=student.objects.get(id=i)
         s.name= data['name']
         s.age= data['age']
         s.course= data['course']
         s.mark= data['mark']
         s.save()
         return JsonResponse({'message':'updated'})

#> PARTIAL UPDATE (PATCH)<

@method_decorator(csrf_exempt, name="dispatch")
class studentpartialupdate(View):
    def patch(self,request,i):
        form_data=request.body
        data=loads(form_data)
        s=student.objects.get(id=i)

        if 'name' in data:
            s.name= data['name']
        if 'age' in data:
            s.age = data['age']
        if 'course' in data:
            s.course = data['course']
        if 'mark' in data:
            s.mark = data['mark']
        s.save()
        return JsonResponse({'message':'partial_updated'})




