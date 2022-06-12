let countrySelected = $('#id_default_country').val();
        if(!countrySelected) {
            $('.select-dropdown').css('color', '#aab7c4');
        };
        
        $('#id_default_country').change(function() {
            countrySelected = $(this).val();
            if(!countrySelected) {
                $('.select-dropdown').css('color', '#aab7c4');
            } else {
                $('.select-dropdown').css('color', '#000');
            }
        });