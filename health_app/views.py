from django.shortcuts import render , redirect , HttpResponse
from . import models
from django.contrib import messages 
import bcrypt
from datetime import datetime
from django.core.mail import send_mail
from my_health.settings import EMAIL_HOST_USER
    

def login(request):
    return render(request , 'login.html')

def loginuser(request):
    if request.method == 'POST':
        if models.Doctor.objects.filter(email = request.POST['email']).exists() == False :
            warnings = models.Patient.objects.login_validator(request.POST)
            if warnings:
                for k , value in warnings.items():
                    messages.warning(request , value)
                return redirect('/')
            else:
                user = models.view_patient(email=request.POST['email'])
                request.session['email'] = user.email
                request.session['id'] = user.id
            return redirect('/pt/'+str(user.id))
        else:
            warnings = models.Doctor.objects.login_validator(request.POST)
            if warnings:
                for k , value in warnings.items():
                    messages.warning(request , value)
                return redirect('/')
            else:
                user = models.view_doctor(email=request.POST['email'])
                request.session['email'] = user.email
                request.session['id'] = user.id
                return redirect('/dr/'+str(user.id))
        
    else:
        return redirect('/')

def signup(request):
    return render(request, 'signup.html')

def create_doctor(request):
    if request.method == 'POST':
        errors = models.Doctor.objects.signup_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request , value)
            return redirect('/signup')
        else:
            if request.POST['account'] == 'Doctor Account':
                new_doctor = models.create_doctor(first_name=request.POST['first_name'] ,last_name=request.POST['last_name'] , email=request.POST['email'], location=request.POST['location'] , password=request.POST['password'] ,dob = request.POST['dob'] , national_id = request.POST['national_id'] , specialty = request.POST['specialty'] , phone_number = request.POST['phone_number'] , gender = request.POST['inlineRadioOptions'] )
                request.session['email'] = request.POST['email']
                request.session['id'] = new_doctor.id
                return redirect('/dr/'+str(new_doctor.id))
            else:
                new_patient = models.create_patient(first_name=request.POST['first_name'] ,last_name=request.POST['last_name'] , email=request.POST['email'] , password=request.POST['password'] ,dob = request.POST['dob'] , national_id = request.POST['national_id'] , phone_number = request.POST['phone_number'] , gender = request.POST['inlineRadioOptions'])
                request.session['email'] = request.POST['email']
                request.session['id'] = new_patient.id
                return redirect('/pt/'+str(new_patient.id))
    else:       
        return redirect('/signup')

def dr_page(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_doctor(id=id).email:
        return redirect('/')
    else:
        context = {
        'dr':models.show_doctor(id = id)
            }
        return render(request ,'dr_page.html',context)


def pt_page(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_patient(id=id).email:
        return redirect('/')
    else:
        context = {
            'pt' : models.show_patient(id=id)
        }
        return render(request , 'pt_page.html' ,context)





def ptinfo_fordoctor(request):
    if request.method == 'POST':
        errors = models.Doctor.objects.national_id_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request , value)
            return redirect('/dr/'+str(request.session['id']))
        else:
            patient = models.pt(national_id = request.POST['national_id'])
            return redirect('/'+patient.first_name +'/'+ str(patient.id))
    else:
        return redirect('/')

def pt_info_for_doctor(request ,name , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_doctor(id=request.session['id']).email:
        return redirect('/')
    else:
        context = {
            'pt': models.show_patient(id=id),
        }
        return render(request, 'pt_info_for_doctor.html',context)


def update_pt_info(request ,id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_doctor(id=request.session['id']).email:
        return redirect('/')
    else:
        age = int(datetime.today().strftime('%Y')) - int(models.show_patient(id=id).dob.strftime('%Y')) 
        context = {
            'pt' : models.show_patient(id =id), 
            'pt_age':  age
        }
        return render(request ,'update_pt_info.html',context)

def update(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_doctor(id=request.session['id']).email:
        return redirect('/')
    else:
        patient = models.show_patient(id=id)
        models.update_information(id=id, pmh=request.POST.get('pmh') , psh=request.POST.get('psh'), current_medications=request.POST.get('current_medications'), allergy=request.POST.get('allergy'))
        return redirect('/'+patient.first_name+'/'+str(id))




def new_visit(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_doctor(id=request.session['id']).email:
        return redirect('/')
    else:
        context = {
        'dr': models.show_doctor(id = request.session['id']),
        'pt':models.show_patient(id=id)
        }
        return render(request , 'new_visit.html' , context)

def create_visit(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_doctor(id=request.session['id']).email:
        return redirect('/')
    else:
        doctor = models.show_doctor(id = request.session['id'])
        patient = models.show_patient(id=id)
        visit = models.create_visit(id=id ,doctor = doctor , patient = patient , cause =request.POST['cause'], management = request.POST['management'] , spo2 = request.POST['spo2'] , hr = request.POST['hr'] , sbp = request.POST['sbp'], dbp = request.POST['dbp'] , temp = request.POST['temp'])
        return redirect('/'+patient.first_name+'/'+str(id))

def visit_info(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    else:
        context = {
            'visit':models.view_visit(id=id)
        }
        return render(request ,'visit_info.html',context)



def vitals(request , id):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    else:
        context = {
            'pt' : models.show_patient(id=id)
        }
        return render(request , 'vitals.html' , context)


def appointment(request , id ):
    if 'id' not in request.session and 'email' not in request.session:
        return redirect('/')
    elif request.session['email'] != models.show_patient(id=id).email:
        return redirect('/')
    else:
        if 'specialty' not in request.session:
            request.session['specialty'] = 0
        if 'location' not in request.session:
            request.session['location'] = 0
        context ={
            'drs':models.all_doctor(),
            'pt': models.show_patient(id=id),
            'specialty':models.doctor_specialty(specialty = request.session['specialty']),
            'the_dr':models.doctor_location(location = request.session['location'] , specialty=request.session['specialty']),
            }
        return render(request , 'appointment.html',context)

def pick_specialty(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        request.session['specialty'] = request.POST['specialty']
        return redirect('/'+str(request.session['id'])+'/appointment')

def pick_location(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        request.session['location'] = request.POST['location']
        return redirect('/'+str(request.session['id'])+'/appointment')

def pick_doctor(request , id):
    if request.method != 'POST':
        return redirect('/')
    else:
        request.session['doctor_id'] = id
        return redirect('/'+str(request.session['id'])+'/appointment')

def make_appointment(request , id):
    if request.method != 'POST':
        return redirect('/')
    else:
        models.make_appointment(id = id ,doctor = models.show_doctor(id = request.session['doctor_id'])   ,patient = models.show_patient(id=id) , location= request.session['location'], date=request.POST['date'])
        subject = 'New Appointment'
        message = f'Dear {models.show_patient(id=id).first_name} you have booked an appointment with Dr. {models.show_doctor(id = request.session['doctor_id']).first_name} in {request.POST['date']} for appointment Cancellation plz visit your account'
        message2 = f'Dear Dr. {models.show_doctor(id = request.session['doctor_id']).first_name} you have a new appointment with {models.show_patient(id=id).first_name}  in {request.POST['date']} for appointment Cancellation plz visit your account'
        email1 = models.show_patient(id=id).email
        email2 = models.show_doctor(id = request.session['doctor_id']).email
        recipient_list = [email1]
        recipient_list2 = [email2]
        send_mail(subject , message , EMAIL_HOST_USER , recipient_list , fail_silently=True)
        send_mail(subject , message2 , EMAIL_HOST_USER , recipient_list2 , fail_silently=True)
        del request.session['specialty']
        del request.session['location']
        del request.session['doctor_id']
        return redirect('/pt/'+str(request.session['id']))

def delete_appointment(request , id):
    appoint = models.show_appointment(id=id)
    doctor = appoint.doctor.email
    if request.session['email'] == doctor:
        models.delete_appointment(id=id)
        return redirect('/dr/'+str(request.session['id']))
    elif request.session['id'] != doctor:
        models.delete_appointment(id=id)
        return redirect('/pt/'+str(request.session['id']))




def logout(request):
    request.session.clear()
    return redirect('/')

