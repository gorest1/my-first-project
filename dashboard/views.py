
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import OrderQueue, KPIRecord
from django.utils import timezone
import json
from django.http import JsonResponse
from datetime import timedelta

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def queue_dashboard(request):
    orders = OrderQueue.objects.order_by('-created_at')[:50]
    return render(request, 'dashboard/queue_dashboard.html', {'orders': orders})

@login_required
def kpi_panel(request):
    # aggregate last 30 days
    since = timezone.now() - timedelta(days=30)
    kpi = KPIRecord.objects.filter(timestamp__gte=since)
    series = {}
    for rec in kpi:
        series.setdefault(rec.metric, []).append([rec.timestamp.isoformat(), rec.value])
    context = {'series_json': json.dumps(series, ensure_ascii=False)}
    return render(request, 'dashboard/kpi_panel.html', context)

def kpi_api(request, metric):
    since = timezone.now() - timezone.timedelta(days=7)
    data = KPIRecord.objects.filter(metric=metric, timestamp__gte=since).order_by('timestamp')
    return JsonResponse({ 'metric': metric,
                          'points': [[rec.timestamp.isoformat(), rec.value] for rec in data] })

@login_required
def shift_schedule(request):
    from .models import ShiftSchedule
    today = timezone.now().date()
    schedule = ShiftSchedule.objects.filter(date__gte=today - timedelta(days=30)).order_by('date','shift')
    return render(request,'dashboard/shift_schedule.html',{'schedule': schedule})

@login_required
def alerts(request):
    from .models import AlertLog
    alerts = AlertLog.objects.all()[:100]
    return render(request,'dashboard/alerts.html',{'alerts':alerts})

@login_required
def reports(request):
    from .models import Report
    reports = Report.objects.order_by('-generated_at')[:20]
    return render(request,'dashboard/reports.html',{'reports':reports})
