from django.urls import path, include

from api.views import *

urlpatterns = [
    path('companies/', get_companies),
    path('companies/<int:id>', get_company),
    path('companies/<int:id>/vacancies', get_vacancy_list_by_company),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:id>', VacancyDetail.as_view()),
    path('vacancies/top_ten/', TopTenVacancies.as_view())
]