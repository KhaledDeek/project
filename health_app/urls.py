from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login),
    path('login/user', views.loginuser),
    path('signup' , views.signup),
    path('signup/account' , views.create_doctor),
    path('dr/<int:id>' , views.dr_page),
    path('pt/<int:id>' , views.pt_page),
    path('<str:name>/<int:id>' , views.pt_info_for_doctor), 
    path('ptinfo' , views.ptinfo_fordoctor),
    path('<int:id>' , views.update_pt_info),
    path('<int:id>/update' , views.update),
    path('<int:id>/visit' , views.new_visit),
    path('<int:id>/new_visit' , views.create_visit),
    path('<int:id>/visit_info' , views.visit_info),
    path('<int:id>/vitals' , views.vitals) , 
    path('<int:id>/appointment' , views.appointment),
    path('specialty' , views.pick_specialty),
    path('location' , views.pick_location),
    path('<int:id>/doctor' , views.pick_doctor),
    path("pt/dr/<int:id>" , views.make_appointment),
    path('<int:id>/visit/delete' , views.delete_appointment),
    path('logout' , views.logout),
]