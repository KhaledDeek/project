const account_type = document.getElementById('selectaccount');
const specialty = document.getElementById('specialty');
const first_name = document.getElementById('first_name');
const last_name = document.getElementById('last_name')
const national_id = document.getElementById('national_id')
const select_location = document.getElementById('select_location')
const email = document.getElementById('email')
const password = document.getElementById('password')
const phone_number = document.getElementById('phone_number')
const dob = document.getElementById('date')
const form = document.getElementById('signupform')
const account_type_error = document.getElementById('account_type_error');
const specialty_error = document.getElementById('specialty_error');
const first_name_error = document.getElementById('first_name_error');
const last_name_error = document.getElementById('last_name_error');
const national_id_error = document.getElementById('national_id_error');
const select_location_error = document.getElementById('select_location_error');
const email_error = document.getElementById('email_error');
const password_error = document.getElementById('password_error');
const phone_number_error = document.getElementById('phone_number_error');
const date_error = document.getElementById('date_error');
const gender = document.getElementsByName('inlineRadioOptions')
const gender_error = document.getElementById('gender_error')

form.addEventListener('submit', (e) => {
    var email_check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (account_type.value == 'Select Account Type') {
        e.preventDefault();
        account_type_error.innerHTML = 'Select Account Type'
    }
    else {
        account_type_error.innerHTML = null
    }
    if (account_type.value == 'Doctor Account' && specialty.value == 'Select Specialty') {
        e.preventDefault();
        specialty_error.innerHTML = 'Select Specialty'
    }
    else {
        specialty_error.innerHTML = null
    }
    if (first_name.value == '' || first_name.value == null) {
        e.preventDefault();
        first_name_error.innerHTML = 'First Name is required '
    }
    else if (first_name.value.length != 0 && first_name.value.length < 2) {
        e.preventDefault();
        first_name_error.innerHTML = 'First Name should be 2 characters at least '
    }
    else {
        first_name_error.innerHTML = null
    }
    if (last_name.value == '' || last_name.value == null) {
        e.preventDefault();
        last_name_error.innerHTML = 'Last Name is required '
    }
    else if (last_name.value.length != 0 && last_name.value.length < 2) {
        e.preventDefault();
        last_name_error.innerHTML = 'last Name should be 2 characters at least '
    }
    else {
        last_name_error.innerHTML = null
    }
    if (national_id.value == '' || national_id.value == null) {
        e.preventDefault();
        national_id_error.innerHTML = 'National ID is required '
    }
    else if (national_id.value.length != 0 && national_id.value.length < 9) {
        e.preventDefault();
        national_id_error.innerHTML = 'National ID should be 9 characters'
    }
    else {
        national_id_error.innerHTML = null
    }
    if (account_type.value == 'Doctor Account' && select_location.value == 'Select Location') {
        e.preventDefault();
        select_location_error.innerHTML = 'Select Location'
    }
    else {
        select_location_error.innerHTML = null
    }
    if (phone_number.value == '' || phone_number.value == null) {
        e.preventDefault();
        phone_number_error.innerHTML = 'Phone Number is required '
    }
    else if (phone_number.value.length != 0 && phone_number.value.length < 10) {
        e.preventDefault();
        phone_number_error.innerHTML = 'Phone Number should be 10 characters'
    }
    else {
        phone_number_error.innerHTML = null
    }
    if (dob.value == '') {
        e.preventDefault();
        date_error.innerHTML = 'Date of Birth is required '
    }
    else {
        date_error.innerHTML = null
    }
    if (gender[0].checked == false && gender[1].checked == false){
        gender_error.innerHTML = 'Select Gender'
    }
    else{
        gender_error.innerHTML = null
    }
    if (!email.value.match(email_check)) {
        e.preventDefault();
        email_error.innerHTML = "Valid Email is required";
    }
    else {
        email_error.innerHTML = null;
    }
    if (password.value == '') {
        e.preventDefault();
        password_error.innerHTML = "Password cant be empty";
    }
    else if (password.value.length != 0 && password.value.length < 8) {
        e.preventDefault();
        password_error.innerHTML = 'Password should be 8 characters at least '
    }
    else {
        password_error.innerHTML = null;
    }

})








function myFunction() {
    let x = document.getElementById("selectaccount").value;
    let inserted = document.getElementById('inserted')
    let location = document.getElementById('location')
    if (x == 'Doctor Account') {
        inserted.style.display = 'flex'
        location.style.display = 'flex';
    }
    else {
        inserted.style.display = 'none'
        location.style.display = 'none';;
    }
}

$(document).ready(function () {
    $("#form").on('submit', function (event) {
        event.preventDefault();
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        });
        $.ajax({
            type: 'POST',
            url: '/signup/account',
            data: {
                account_type: $("#selectaccount").val(),
                password: $('#password').val(),
                select_specialty: $('#select').val(),
                first_name: $("#first_name").val(),
                last_name: $("#last_name").val(),
                national_id: $("#national_id").val(),
                location: $("#location").val(),
                email: $("#email").val(),
                password: $('#password').val(),
                phone_number: $("#phone_number").val(),
                date: $('#date').val(),
                gender: $('inlineRadioOptions').val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});