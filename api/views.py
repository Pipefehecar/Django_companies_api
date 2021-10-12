import json
from django.http.response import JsonResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company
import json 
# Create your views here.

class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):#read
        if (id>0):
            companies= list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]
                datos={'menssage':"success",'company':company}
            else:
                datos={'menssage':"company not found.."}  
            return JsonResponse(datos)
        else:        
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos={'menssage':"success",'companies':companies}
            else:
                datos={'menssage':"companies not found.."}  
            return JsonResponse(datos)

    def post(self,request):#create
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        datos={'menssage':"success"}
        return JsonResponse(datos)

    def put(self,request,id):#update
        jd = json.loads(request.body)
        companies= list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos={'menssage':"success"}
        else:
            datos={'menssage':"company not found.."}  
        return JsonResponse(datos)
    def delete(self,request,id):
        companies= list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.delete()
            datos={'menssage':"success"}
        else:
            datos={'menssage':"company not found.."}  
        return JsonResponse(datos)