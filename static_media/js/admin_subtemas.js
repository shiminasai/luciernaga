(function($) {

var carlos = $('#id_subtema').select2('data');
var currentLocation = window.location.pathname.split('/');
//alert(currentLocation[5]);

var foo = [];
$(document).on('change','#id_temas',function(){

    $('#id_temas :selected').each(function(i, selected){
        foo[i] = $(selected).val();
        //console.log(foo[i]);
    });

    $.getJSON('/ajax/subtemas/?ids='+foo.join(","), function(data){
        //console.log(data);
        if (currentLocation[5] == 'change' )
        {
            $('#id_subtema').html('');
        }else {
            $('#id_subtema').html('');
        }

        $('#id_subtema').select2();
        var subtemas = $('#id_subtema')
        if(data){

           $.each(data, function(i, item){
            $.each(item, function(j, item2){
                var group = $('<optgroup></optgroup>').attr('label', j);
                group.append($('<option></option>').val(item2.id).html(item2.nombre));

                group.appendTo(subtemas);
                $('#id_subtema').select2();
            });
        });

       }
   });
});


})(django.jQuery);
