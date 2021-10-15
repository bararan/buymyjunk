$('input:checkbox').on('change', function() {
    $('input:checkbox').not(this).prop('checked', false);
 });

 $(document).on('click', '.confirm-delete', ()=> {
     return confirm('Are you sure you want to delete this item?');
 })