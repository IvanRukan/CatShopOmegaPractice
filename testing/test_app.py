from CatModels import get_cat_for_tests
from UserModels import get_user, numeric_value_from_string
from main import app


def test_new_user(client):
    response = client.post('/register', data={
        'name': 'pytest name',
        'email': 'pytest@gmail.com',
        'password': 'pytest password',
        
    }, follow_redirects=True)
    with app.app_context():
        assert get_user(str(numeric_value_from_string('pytest@gmail.com'))[0:17]) is not None


def test_login_user(client):
    response = client.post('/login', data={
        'name': 'pytest name',
        'email': 'pytest@gmail.com',
        'password': 'pytest password',
    }, follow_redirects=True)
    assert response.status_code == 200


def test_add_cat_new(client):
    response = client.post('/add', data={
        'name': 'TEST CAT',
        'breed': 'TEST BREED',
        'gender': 'TEST GENDER',
        'color': 'TEST COLOR',
        'age': '3',
        'cost': '777'
    }, follow_redirects=True)
    with app.app_context():
        assert get_cat_for_tests('TEST CAT') is not None


def test_edit_cat(client):
    with app.app_context():
        cat = get_cat_for_tests('TEST CAT')
    response = client.post(f'/edit_chosen_cat/{cat.id}', data={
        'name': 'edited TEST CAT',
        'breed': 'edited TEST BREED',
        'gender': 'edited TEST GENDER',
        'color': 'edited TEST COLOR',
        'age': '15',
        'cost': '999'
    }, follow_redirects=True)
    with app.app_context():
        assert get_cat_for_tests('edited TEST CAT') is not None


def test_get_cat(client):
    with app.app_context():
        cat = get_cat_for_tests('edited TEST CAT')
    response = client.get(f'/{cat.id}')
    assert response.status_code == 200


def test_delete_cat(client):
    with app.app_context():
        cat = get_cat_for_tests('edited TEST CAT')
    response = client.get(f'/delete_chosen_cat?id={cat.id}', follow_redirects=True)
    with app.app_context():
        assert get_cat_for_tests('edited TEST CAT') is None


