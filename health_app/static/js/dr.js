x = document.getElementById('imgx')
x.src = '/static/images/HD-wallpaper-purple-waves-abstract-kor4-rts-background-black-pattern-pink-wave.jpg'
$(document).ready(function () {
    $("#form").on('submit', function (event) {
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
            url: '/ptinfo',
            data: {
                national_id: $("#national_id").val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});