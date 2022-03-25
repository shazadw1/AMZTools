$(document).ready(function() {
    $.ajax({
        headers: {
            "X-CSRFToken": '{{csrf_token}}'
        },
        type: 'POST',
        url: '/address',
        data: {
            'text': txt,
            'post_id': id
        },
        success: function(response) {
            document.getElementById().value = '';
        },
        error: function(response) {
            console.log(response)
        }
    });
});