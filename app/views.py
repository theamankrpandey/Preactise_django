from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import io
# Create your views here.
# @csrf_exempt
# def stui(req):
#     if req.method == "POST":
#         data = req.body
#         # JSON bytes -> Python dictionary
#         p_data = json.loads(data)
#         print(data)
#         if 'name' in p_data and 'age' in p_data and 'email' in p_data and 'contact' in p_data:
#             n = p_data.get("name")
#             a = p_data.get("age")
#             e = p_data.get("email")
#             c = p_data.get("contact")

#             Student.objects.create(
#                 name = n,age=a,email=e,contact=c
#             )
#             return JsonResponse("data Created Successfully",safe=False)
#         else:
#             j = "something went Wrong"
#             return JsonResponse(j,safe=False)
#     else:
#         data = Student.objects.all().values()
#         # list me bana kr bhej rhe hai jsonresponse me 
#         # print(p_data)
#         # print(p_data.values_list())
#         # print(p_data.values())
#         j_data = list(data)
#         # print(j_data)

#         # return JsonResponse(j_data) # TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
#         return JsonResponse(j_data, safe=False)




# @csrf_exempt
# def stu(req,pk):
#     data = req.body
#     p_data = json.loads(data)
#     User = Student.objects.get(id=pk)
#     if not User:
#         return JsonResponse("User Not In our Db")
#     if req.method == "PUT":
#         n = p_data.get("name")
#         a = p_data.get("age")
#         e = p_data.get("email")
#         c = p_data.get("contact")
#         if "name" in p_data and "age" in p_data and "email" in p_data and "contact" in p_data:
#             data = Student.objects.get(id=pk)
#             data.name = n
#             data.age = a
#             data.email = e
#             data.contact = c
#             return JsonResponse("data updated succesfully",safe=False)
#         else:
#             return JsonResponse("Required Field Are Missing",safe=False)
#     if req.method=="PATCH":
#         if "name" in p_data:
#             return JsonResponse("Name Updated Succesfully",safe=False)
#         if "age" in p_data:
#             return JsonResponse("age Updated Succesfully",safe=False)
#         if "email" in p_data:
#             return JsonResponse("email Updated Succesfully",safe=False)
#         if "contact" in p_data:
#             return JsonResponse("contact Updated Succesfully",safe=False)
#         else:
#             # data3 = Student.objects.get(id=pk)
#             # data3.delete()
#             return JsonResponse("Some Required Are Mising",safe=False)
#     else:
#         User.delete()
#     return JsonResponse("Data Deletd Succesfully",safe=False)



# def product(request):
#     item = Item.objects.all()
#     return render(request, "cart.html",{"item":item})


# def cart(request,pk):
#     data = Item.objects.get(id=pk)
#     if "cart_count" not in request.session:
#         request.session["cart_count"] = 0
#     else:
#         if request.method == "POST":
#             request.session["cart_count"] += 1
#         return render(request, "cart.html",{
#             "data":data,
#             'cart_count':request.session["cart_count"]
#             })

# def Decrement(req):
#     if "cart_count" not in req.session:
#         req.session['cart_count'] = 0
#     else:
#         if req.session['cart_count']>0:
#             req.session['cart_count'] -=1
#     return render(req,"cart.html",{"cart_count":req.session['cart_count']})


# def Increment(req):
#     if "cart_count" not in req.session:
#         req.session['cart_count'] = 0
#     else:
#         if req.session['cart_count']>0:
#             req.session['cart_count'] +=1
#     return render(req,"cart.html",{"cart_count":req.session['cart_count']})



@csrf_exempt
def item (req,pk):
    user = Item.objects.filter(id=pk)
    if not user:
        return JsonResponse("User Not exist In our Db",safe=False)
    if req.method == "PUT":
        j_data = req.body
        p_data = json.loads(j_data)
        if 'Name' in p_data and 'Quantity' in p_data:
            n = p_data.get('Name')
            q = p_data.get('Quantity')
            old_data = Item.objects.get(id=pk)
            old_data.Name = n
            old_data.Quantity = q
            old_data.save()
            return JsonResponse("Data Updated Succesfully",safe=False)
        return JsonResponse("Some Required Field Are Missing",safe=False)
    
    if req.method=="PATCH":
        j_data = req.body
        p_data = json.loads(j_data)
        if p_data:
            n = p_data.get('Name')
            q = p_data.get('Quantity')
            old_data = Item.objects.get(id=pk)
            if n and q:
                old_data.Name = n
                old_data.Quantity = q
                old_data.save()
                return JsonResponse("Name And Quantity Updated Succesfully",safe=False)
            if n:
                old_data.Name = n
                old_data.save()
                return JsonResponse("Name Updated Succesfully",safe=False)
            if q:
                old_data.Quantity = q
                old_data.save()
                return JsonResponse(" Quantity Updated Succesfully",safe=False)
            return JsonResponse(" Some Required Field Are Wrong",safe=False)
        return JsonResponse("Something Went Wrong")
    
    if req.method=="DELETE":
        user = Item.objects.get(id=pk)
        user.delete()
        return JsonResponse("object Deleted",safe=False)
    p_data = Item.objects.get(id=pk)    
    j_data = model_to_dict(p_data)
    return JsonResponse(j_data)