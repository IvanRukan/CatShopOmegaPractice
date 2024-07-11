

function choose_cat() {
    $.ajax({
        type: 'GET',
        url: '/delete_chosen_cat',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            'id': document.getElementById('cat_id').innerHTML,
        },
        complete: function (response) {
                    alert("You will now be redirected.");
                    window.location.href = '/';
        }
    });
}


function edit_cat() {
    $.ajax({
        type: 'GET',
        url: '/edit_chosen_cat',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            'id': document.getElementById('cat_id').innerHTML,
        },
        success: function (response) {
            console.log(response['ID'])
            window.location.href = '/edit_chosen_cat/' + response['ID']
        }
    });
}


document.getElementById('choose_cat').addEventListener('click', choose_cat)
document.getElementById('edit_cat').addEventListener('click', edit_cat)

