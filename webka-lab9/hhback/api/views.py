from django.shortcuts import render
from api.models import Company, Vacancy
from django.http.response import HttpResponse, JsonResponse

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return  JsonResponse({'message': str(e)}, status =400)
    return JsonResponse(company.to_json())

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as p:
        return  JsonResponse({'message': str(p)}, status =400)
    return JsonResponse(vacancy.to_json())

# def vacancylist_from_company(request, company_id):
#     try:
        
#     except


def vacancy_topten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def from_company_vacancy(request, company_id):
    vacancies = Vacancy.objects.filter(company = company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)