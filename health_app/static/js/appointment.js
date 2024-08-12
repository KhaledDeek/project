x = document.getElementById('imgx')
x.src = '/static/images/appointment.jpg'
$(document).ready(function () {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});

$(document).ready(function () {
    $("#specialty_form").on('change', function (event) {
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
            type: 'GET',
            url: '/specialty',
            data: {
                '<%Session["id"]' : $('#pt_id').val(),
                '<%Session["specialty"]' : $("#specialty").val(),
                specialty: $("#specialty").val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function (data) {
                allert('data')
            }
        })
    })
});
$(document).ready(function () {
    $("#location_form").on('change', function (event) {
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
            url: '/location',
            data: {
                '<%Session["location"]' : $('#location').val(),
                location: $('#location').val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});

$(document).ready(function () {
    $("#doctor_form").on('change', function (event) {
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
            url: '/doctor',
            data: {
                '<%Session["doctor_id"]': $('#dr').val(),
                dr: $('#dr').val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});

/*$(document).ready(function () {
    $("#appointment_form").on('submit', function (event) {
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
            url: '/pt/dr/'+$('#pt_id').val(),
            data: {
                "request.session['id']" :  '<%Session["id"]',
                "request.session['specialty']" : '<%Session["specialty"]',
                "request.session['doctor_id']" : '<%Session["doctor_id"]',
                "request.session['location']" : '<%Session["location"]',
                date : $('#date').val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});*/


