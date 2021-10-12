from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CompanyView
urlpatterns = [
    path('companies/',CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(), name='companies_process')
]