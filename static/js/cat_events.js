

function choose_cat() {
    $.ajax({
        type: 'GET',
        url: '/delete_chosen_cat',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            'id': document.getElementById('cat_id').innerHTML,
        },
        success: function (response) {

        }
    });
}

document.getElementById('choose_cat').addEventListener('click', choose_cat)

