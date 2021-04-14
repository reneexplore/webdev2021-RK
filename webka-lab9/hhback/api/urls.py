from django.urls import path, re_path

from api.views import company_list,company_detail
from api.views import vacancy_detail, vacancy_list
from api.views import vacancy_topten, from_company_vacancy


urlpatterns = [
    path('api/companies', company_list),
    path('api/companies/<int:company_id>/', company_detail),
    path('api/vacancies', vacancy_list),
    path('api/vacancies/<int:vacancy_id>/', vacancy_detail),
    path('api/vacancies/top_ten/',vacancy_topten ),
    path('api/companies/<int:company_id>/vacancies', from_company_vacancy)
]