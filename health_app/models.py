from django.db import models
from django.contrib import messages 
from django.db import models
import re
import bcrypt
from datetime import datetime


class UserManager(models.Manager):
    def signup_validator(self , postData):
        errors = {}
        if postData['account'] == 'Select Account Type':
            errors['account'] = 'Please Select Account Type'
        if postData['account'] == 'Doctor Account':
            if postData['specialty'] == '':
                errors['specialty'] = 'Please Select A Specialty'
        if len(postData['first_name']) < 2 : 
            errors['first_name'] = 'First Name must be at least 2 characters '
        if len(postData['last_name']) < 2 : 
            errors['last_name'] = 'Last Name must be at least 2 characters '
        if len(postData['national_id']) < 9 : 
            errors['national_id'] = 'National ID should be at least 9 characters'
        if len(postData['password']) < 8 : 
            errors['password'] = 'Password should be at least 8 characters'
        if len(postData['phone_number']) < 10 : 
            errors['phone_number'] = 'Phone number should be at least 10 characters'
        elif Doctor.objects.filter(phone_number = postData['phone_number']).exists() or Patient.objects.filter(phone_number = postData['phone_number']).exists() : 
            errors['phone_number'] = 'Phone number already Registered'        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = "Invalid email address!"
        if Doctor.objects.filter(email = postData['email']).exists() or Patient.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email already exists"
        if len(postData['national_id']) == 0:
            errors['national_id'] = 'National Id cant be empty'
        elif Doctor.objects.filter(national_id = postData['national_id']).exists() or Patient.objects.filter(national_id = postData['national_id']).exists() : 
            errors['national_id'] = 'National ID already Registered'
        return errors
    def login_validator(self , postData):
        warnings = {}
        if postData['email'] == '':
            warnings['email'] = 'Email field cant be empty'
        elif postData['password'] == '':
            warnings['password'] = 'Password field cant be empty'
        elif Doctor.objects.filter(email = postData['email']).exists()== False and Patient.objects.filter(email = postData['email']).exists() == False :
            warnings['email'] = "Email does not exist"
        elif Doctor.objects.filter(email = postData['email']).exists()== True:
            if bcrypt.checkpw(postData['password'].encode(),view_doctor(email = postData['email']).password.encode()) == False:
                warnings['password'] = 'Incorrect Email/Password'
        elif Patient.objects.filter(email = postData['email']).exists() == True :
            if bcrypt.checkpw(postData['password'].encode(),view_patient(email = postData['email']).password.encode()) == False:
                warnings['password'] = 'Incorrect Password'
        return warnings
    def national_id_validator(self , postData):
        errors = {}
        if postData['national_id'] == '':
            errors['national_id'] = 'Enter National ID '
        elif Patient.objects.filter(national_id = postData['national_id']).exists() == False : 
            errors['national_id'] = 'National ID does not exists'
        return errors



class Doctor(models.Model):
    first_name = models.CharField(max_length=50 , error_messages={'required':'A contact needs a first name.'})
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    national_id = models.IntegerField()
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=8)
    specialty = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    national_id = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Information(models.Model):
    patient = models.OneToOneField(Patient ,related_name="informations", on_delete=models.CASCADE , primary_key=True)
    pmh = models.TextField(default="New Patient")
    psh = models.TextField(default='New Patient')
    allergy = models.TextField(default='New Patient')
    current_medications = models.TextField(default='New Patient')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Visit(models.Model):
    doctor = models.ForeignKey(Doctor ,related_name='visit', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient ,related_name='visit', on_delete=models.CASCADE)
    cause = models.TextField(default='Visit was not established yet ')
    management= models.TextField(default='Visit was not established yet')
    location = models.TextField(default='Location')
    date = models.DateField(default=datetime.today())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor ,related_name='appoint', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient ,related_name='appoint', on_delete=models.CASCADE)
    location = models.TextField(default='Location')
    date = models.DateField(default=datetime.today())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vital(models.Model):
    visit = models.OneToOneField(Visit ,related_name="vitals", on_delete=models.CASCADE , primary_key=True)
    patient = models.ForeignKey(Patient , related_name='vitals' , on_delete=models.CASCADE)
    hr = models.IntegerField()
    sbp = models.IntegerField()
    dbp = models.IntegerField()
    temp = models.FloatField()
    spo2 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





def create_doctor(first_name , last_name ,specialty, national_id , email , password , phone_number , dob , gender , location):
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return Doctor.objects.create(first_name = first_name , last_name = last_name, specialty = specialty, location = location  , national_id = national_id , email = email , password = pw_hash  , phone_number = phone_number , dob = dob , gender = gender)

def view_doctor(email):
    return Doctor.objects.get(email = email)

def show_doctor(id):
    return Doctor.objects.get(id=id)

def doctor_name(name):
    return Doctor.objects.get()

def all_doctor():
    return Doctor.objects.all()

def create_patient(first_name , last_name , national_id , email , password , phone_number , dob , gender):
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    patient = Patient.objects.create(first_name = first_name , last_name = last_name , national_id = national_id , email = email , password = pw_hash  , phone_number = phone_number , dob = dob , gender = gender )
    return patient

def view_patient(email):
    return Patient.objects.get(email = email)

def show_patient(id):
    return Patient.objects.get(id=id)

def pt(national_id):
    return Patient.objects.get(national_id=national_id)

def update_information(id, pmh , psh , allergy , current_medications):
    if Information.objects.filter(patient = show_patient(id=id)).exists() == True:
        info = show_patient(id=id).informations
        info.pmh=pmh
        info.psh= psh
        info.allergy= allergy
        info.current_medications = current_medications
        return info.save()
    else:
        patient = show_patient(id=id)
        return Information.objects.create(patient = patient ,pmh = pmh , psh =psh , allergy = allergy , current_medications = current_medications)

def create_visit(id , doctor , patient, cause , management , hr, spo2 , temp , sbp , dbp):
    visit = Visit.objects.create(doctor = doctor , patient =patient , cause = cause , management = management )
    vitals = Vital.objects.create(hr = hr , spo2 = spo2 , temp = temp , sbp = sbp , dbp = dbp ,  visit = visit , patient = patient )
    return visit , vitals

def view_visit(id):
    return Visit.objects.get(id=id)



def doctor_specialty(specialty):
    return Doctor.objects.filter(specialty = specialty)


def doctor_location(location , specialty):
    return Doctor.objects.filter(location = location).filter(specialty = specialty)


def make_appointment(id ,doctor , patient , location , date ):
    return Appointment.objects.create(doctor = doctor , patient = patient , location = location , date = date  )

def delete_appointment(id):
    appoint = Appointment.objects.get(id=id)
    return appoint.delete()

def show_appointment(id):
    return Appointment.objects.get(id=id)