from api.models import Service
from api.models import Client
from api.models import Master
from api.models import Appointment
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_appointment(request):
    """Add appointment record to the database"""
    if request.method == "POST":
        client_name = request.POST['client_name']
        client_phone = request.POST['client_phone']
        client, is_created = Client.objects.get_or_create(name=client_name, phone_number=client_phone)
        
        master_name = request.POST['master']
        master, is_created = Master.objects.get_or_create(name=master_name)

        service_name = request.POST['service']
        service, is_created = Service.objects.get_or_create(name=service_name)
        
        appointment_datetime = request.POST['datetime']
        appointment = Appointment(client=client, service=service, master=master, appointment_datetime=appointment_datetime)
        appointment.save()
    return render(request, 'empty.html')




@csrf_exempt
def show_appointments(request):
    """Show all appointments as a table"""
    appointments = Appointment.objects.all()
    records = []
    for appointment in appointments:
        dt = appointment.appointment_datetime
        records.append(dict(client_name=appointment.client.name,
                            client_phone=appointment.client.phone_number,
                            service=appointment.service.name,
                            master=appointment.master.name,
                            appointment_datetime=dt.strftime("%Y-%m-%d %H:%M:%S")))         
    return render(request, 'showall.html', {
        'appointments': records
    })
