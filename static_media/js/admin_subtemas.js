(function($) {

var currentLocation = window.location.pathname.split('/');

var foo = [];
$(document).on('change','#id_temas',function(){

    var count = $('#id_subtema option:selected').length;
    console.log(count);

    $('#id_temas :selected').each(function(i, selected){
        foo[i] = $(selected).val();
    });

    $.getJSON('/ajax/subtemas/?ids='+foo.join(","), function(data){

        if (currentLocation[5] == 'change' && count >= 1)
        {

        }else {
            $('#id_subtema').html('');
        }
        //$('#id_subtema').html('');
        $('#id_subtema').select2();
        var subtemas = $('#id_subtema');
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
