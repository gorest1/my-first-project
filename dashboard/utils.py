
from django.http import HttpResponse
import csv, openpyxl, io, datetime
from .models import OrderQueue

def export_orders_xlsx():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['ID', 'Client', 'Status', 'Created'])
    for o in OrderQueue.objects.all():
        ws.append([o.id, o.client, o.get_status_display(), o.created_at.strftime('%d.%m.%Y %H:%M')])
    bio = io.BytesIO()
    wb.save(bio)
    bio.seek(0)
    response = HttpResponse(
        bio.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="orders.xlsx"'
    return response
