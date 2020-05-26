$('.dataTable').DataTable(
    {
        paging: false,
        searching: false
    });
$('#Table_info').hide();

$(document).ready(function(){
    $("#Table").on('click','#btnTraduci',function(){
        var currentRow=$(this).closest("tr");
        var text=currentRow.find(".termine").html();
        var lang= 'it-'+ document.getElementById('lang_codes').value;
        $.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200419T153943Z.f77eeeb739cd8e92.317561bb1083e531f4a8d9631e9ca7e76933f79a&text='+text+'&lang='+lang, function(result){
            currentRow.find('#result').html(result.text);
        })
    });
});





