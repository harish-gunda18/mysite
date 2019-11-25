from companies.api.views import api_detail_company_view
from django.urls import path

app_name = 'companies'

urlpatterns = [
    path('<ticker>/', api_detail_company_view, name='detail')
]
