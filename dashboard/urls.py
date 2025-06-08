
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    path('schedule/', views.shift_schedule, name='schedule'),
    path('alerts/', views.alerts, name='alerts'),
    path('reports/', views.reports, name='reports'),

    path('', views.home, name='home'),
    path('queue/', views.queue_dashboard, name='queue'),
    path('kpi/', views.kpi_panel, name='kpi'),
    path('api/kpi/<str:metric>/', views.kpi_api, name='kpi_api'),
]
