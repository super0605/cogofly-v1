(function($) {
$(document).ready(function() {
    var mn=30, mx=2000,
        ch=function() {
        var v=$(this).val();
        if ((v<mn) || (v>mx)) {
            return;
        }
        var p = $(this).parent().find('select[multiple]');
        if (p.outerHeight()!=v) p.outerHeight(v);
    };
    $('select[multiple]').each(function() {
        $(this)
            .parent()
            .append(
                $('<input type="number" min="'+mn+'" />')
                    .css({'width':'50px',
                          'margin':'6px',
                          'display':'block',
                          'float':'right'})
                    .val($(this).outerHeight())
                    .change(ch).keyup(ch)
            );
    });
});
})(django.jQuery);

