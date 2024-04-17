from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(['GET'])
def get_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_company(request, id):
    company = get_object_or_404(Company, pk=id)
    serializer = CompanySerializer(company)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_vacancy_list_by_company(request, id):
    company = get_object_or_404(Company, pk=id)
    vacancies = company.vacancy_set.all()
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

class VacancyList(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

class VacancyDetail(APIView):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, pk=id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

class TopTenVacancies(APIView):
    def get(self, request):
        top_ten_vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_ten_vacancies, many=True)
        return Response(serializer.data)