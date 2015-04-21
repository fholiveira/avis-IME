(function() {
    var lista = $('li');

    $('input[type=search]').keyup(function(e) {
        var text = $(this).val().toLowerCase();

        if (!text.length) {
            lista.removeClass('hidden');
            return;
        }

        lista.each(function(i, el) {
           var listItem = $(el);
           var itemText = listItem.text().toLowerCase();

           if (itemText.indexOf(text) > 0) {
               listItem.removeClass('hidden');   
           } else {
               listItem.addClass('hidden');
           }
        });
    })

     $('input[type=checkbox]').change(function() {
        if (this.checked) {
            $.post('/feed', { id: this.id.substr(1) });
    
            return;
        } 

        $.ajax({
            url: '/feed',
            method: 'DELETE',
            data: {id: this.id.substr(1) }
        });
     });

})();
