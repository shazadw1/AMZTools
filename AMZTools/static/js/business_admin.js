$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});


function SubmitForm(){
        $.ajax({
          headers: {
            "X-CSRFToken": '{{csrf_token}}'
          },
          type: 'POST',
          url: '/address',
          data : $('#address_form').serialize(),
          success: function(response){
            if (response.resp=='Address Added successfully !!'){
                alert(response.resp);
                document.getElementById('address_form').style.display = 'none';
//                var checkboxValues = [];
//                $('input[type=checkbox]:checked').map(function() {
//                    checkboxValues.push($(this).attr('name'));
//                });
//                console.log(checkboxValues)
                optionValues0 = {"1": {id: response.pk, value: $('#id_street1').val()+$('#id_street2').val()+$('#id_area').val()+$('#id_city').val()+$('#id_state').val()}};
                $.each(optionValues0, function(order, object) {
                  key = object.id;
                  value = object.value;
                    $('#id_registered_address').append($('<option>', { value : key }).text(value));
                    $('#id_trading_address').append($('<option>', { value : key }).text(value));
                    $('#id_director1_address').append($('<option>', { value : key }).text(value));
                    $('#id_director2_address').append($('<option>', { value : key }).text(value));
                });
                $("#address_form")[0].reset()

            }
            else{
                alert(response.resp);
            }
          }
        });
        return false;
};
