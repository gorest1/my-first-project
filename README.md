
# Bazis Monitoring & KPI Dashboard

A Django‑based web application for real‑time monitoring of the order queue and key production metrics of **ООО «БАЗИС‑ЦЕНТР»**.

## Quick start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_data.json  # optional demo data
python manage.py runserver
```

* Default users (see `fixtures/initial_users.json`)  
  * **admin** / `admin123` — full access  
  * **manager** / `manager123` — queue & KPI dashboards, document export  
  * **client** / `client123` — personal cabinet and order status  

Full documentation is in `/docs`.


### Новые страницы
* **/schedule/** — производственный календарь/график смен  
* **/alerts/** — журнал инцидентов  
* **/reports/** — список отчётов (.docx, .xlsx и др.)

Демо‑данные для этих разделов входят в `sample_data.json`.
