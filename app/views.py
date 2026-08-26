from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Student 
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
@csrf_exempt
def stui(req):
    if req.method == "POST":
        data = req.body
        # JSON bytes -> Python dictionary
        p_data = json.loads(data)
        print(data)
        if 'name' in p_data and 'age' in p_data and 'email' in p_data and 'contact' in p_data:
            n = p_data.get("name")
            a = p_data.get("age")
            e = p_data.get("email")
            c = p_data.get("contact")

            Student.objects.create(
                name = n,age=a,email=e,contact=c
            )
            return JsonResponse("data Created Successfully",safe=False)
        else:
            j = "something went Wrong"
            return JsonResponse(j,safe=False)
    else:
        data = Student.objects.all().values()
        # list me bana kr bhej rhe hai jsonresponse me 
        # print(p_data)
        # print(p_data.values_list())
        # print(p_data.values())
        j_data = list(data)
        # print(j_data)

        # return JsonResponse(j_data) # TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
        return JsonResponse(j_data, safe=False)




@csrf_exempt
def stu(req,pk):
    data = req.body
    p_data = json.loads(data)
    User = Student.objects.get(id=pk)
    if not User:
        return JsonResponse("User Not In our Db")
    if req.method == "PUT":
        n = p_data.get("name")
        a = p_data.get("age")
        e = p_data.get("email")
        c = p_data.get("contact")
        if "name" in p_data and "age" in p_data and "email" in p_data and "contact" in p_data:
            data = Student.objects.get(id=pk)
            data.name = n
            data.age = a
            data.email = e
            data.contact = c
            return JsonResponse("data updated succesfully",safe=False)
        else:
            return JsonResponse("Required Field Are Missing",safe=False)
    if req.method=="PATCH":
        if "name" in p_data:
            return JsonResponse("Name Updated Succesfully",safe=False)
        if "age" in p_data:
            return JsonResponse("age Updated Succesfully",safe=False)
        if "email" in p_data:
            return JsonResponse("email Updated Succesfully",safe=False)
        if "contact" in p_data:
            return JsonResponse("contact Updated Succesfully",safe=False)
        else:
            # data3 = Student.objects.get(id=pk)
            # data3.delete()
            return JsonResponse("Some Required Are Mising",safe=False)
    else:
        User.delete()
    return JsonResponse("Data Deletd Succesfully",safe=False)
