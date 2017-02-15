(function ($) {

    function initSelect2Sortable(selectElement) {
        selectElement.select2();
        var choices = selectElement.prev('.select2-container').find('ul.select2-choices');

        var valueChangeObserver = new MutationObserver(function (mutations) {
            choices.sortable({
                forcePlaceholderSize: true,
                items: 'li.select2-search-choice',
                placeholder: '<li>&nbsp;</li>'
            });
            valueChangeObserver.disconnect();
        });

        selectElement.on('select2-selecting', function () {
            valueChangeObserver.observe(choices.get(0), {subtree: false, childList: true, attributes: false});
        });
        choices.sortable({
            forcePlaceholderSize: true,
            items: 'li.select2-search-choice',
            placeholder: '<li>&nbsp;</li>'
        });
        choices.bind('sortupdate', function (e, ui) {
            $(choices.find('li.select2-search-choice').get().reverse()).each(function () {
                var id = $(this).data('select2Data').id,
                    $option = options.selectElement.find('option[value="' + id + '"]')[0];

                options.selectElement.prepend($option);
            });
        });

        selectElement.data('hasSelect2Sortable', true);
    };


    function sortSelect2Sortable(selectElement, val) {
        var choices = selectElement.prev('.select2-container').find('ul.select2-choices');
        var searchChoices = choices.find('.select2-search-choice');

        $.each(val, function (i, id) {
            searchChoices.each(function () {
                if (id == $(this).data('select2Data').id) {
                    $(this).insertBefore(choices.find('.select2-search-field'));
                }
            });
        });

        choices.trigger('sortupdate');
    }

    $.fn.extend({
        select2Sortable: function (val) {
            this.each(function () {
                var selectElement = $(this);
                // Only sort multiple selects
                if (!selectElement.prop('multiple')) {
                    if (!selectElement.data('hasSelect2Sortable')) {
                        choices.sortable({
                            forcePlaceholderSize: true,
                            items: 'li.select2-search-choice',
                            placeholder: '<li>&nbsp;</li>'
                        });

                        if (selectElement.attr('data-order')) {
                            sortSelect2Sortable(selectElement, selectElement.attr('data-order').split(','));
                        }
                    }
                    if (val) {
                        sortSelect2Sortable(selectElement, val);
                    }
                }
            });

            return this;
        }
    });
}(jQuery));
