x = document.getElementById('imgx')
x.src = '/static/images/HD-wallpaper-purple-waves-abstract-kor4-rts-background-black-pattern-pink-wave.jpg'
const cause = document.getElementById('form1')
const cause_error = document.getElementById('cause_error')
const management = document.getElementById('form2')
const hr = document.getElementById('a')
const temp = document.getElementById('b')
const spo2 = document.getElementById('f')
const sbp = document.getElementById('d')
const dbp = document.getElementById('e')
const hr_error = document.getElementById('a_error')
const temp_error = document.getElementById('b_error')
const spo2_error = document.getElementById('f_error')
const sbp_error = document.getElementById('d_error')
const dbp_error = document.getElementById('e_error')
const form = document.getElementById('pt_info_form')

form.addEventListener('submit', (e) => {
    if (cause.value == '' || cause.value == null){
        e.preventDefault();
        cause_error.innerHTML = 'Enter The Cause'
    }
    else{
        cause_error.innerHTML = null;
    }
    if (management.value == '' || management.value == null){
        e.preventDefault();
        management_error.innerHTML = 'Enter The Management'
    }
    else{
        management_error.innerHTML = null;
    }
    if(hr.value == '' || hr.value == null){
        e.preventDefault();
        hr_error.innerHTML = "HR ?"
    }
    else{
        hr_error.innerHTML = null
    }
    if(temp.value == '' || hr.value == null){
        e.preventDefault();
        temp_error.innerHTML = "Temp ?"
    }
    else{
        temp_error.innerHTML = null
    }
    if(spo2.value == '' || hr.value == null){
        e.preventDefault();
        spo2_error.innerHTML = "Spo2 ?"
    }
    else{
        spo2_error.innerHTML = null
    }
    if(sbp.value == '' || hr.value == null){
        e.preventDefault();
        sbp_error.innerHTML = "SBP ?"
    }
    else{
        sbp_error.innerHTML = null
    }
    if(dbp.value == '' || hr.value == null){
        e.preventDefault();
        dbp_error.innerHTML = "DBP ?"
    }
    else{
        dbp_error.innerHTML = null
    }
})