
$("#booking-form").validate();
 
$("#checkin").datepicker({
        defaultDate: "+1w",
        changeMonth: false,
        numberOfMonths: 1,
        prevText: '<i class="fa fa-chevron-left"></i>',
        nextText: '<i class="fa fa-chevron-right"></i>',
        onClose: function( selectedDate ) {
                $( "#checkout" ).datepicker( "option", "minDate", selectedDate );
        }
});
 
$("#checkout").datepicker({
        defaultDate: "+1w",
        changeMonth: false,
        numberOfMonths: 1,
        prevText: '<i class="fa fa-chevron-left"></i>',
        nextText: '<i class="fa fa-chevron-right"></i>',                    
        onClose: function( selectedDate ) {
                $( "#checkin" ).datepicker( "option", "maxDate", selectedDate );
        }
});
