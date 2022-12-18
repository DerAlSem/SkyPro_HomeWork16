from app import app

# Get запросы не тестировал - их проще и быстрее посмотреть в браузере. :) А вот post, put и delete тестами покрыты
def test_user_method_post():
    test_user_json = {'id': 1030,
                      'first_name': 'Alexey',
                      'last_name': 'Derevyanko',
                      'age': 28,
                      'email': 'nospam@gmail.com',
                      'role': 'executor',
                      'phone': '123123123'}
    resp = app.test_client().post('/users', json=test_user_json)
    assert resp.status_code == 200

def test_user_method_put():
    test_user_json = {'id': 1,
                      'first_name': 'Hudson',
                      'last_name': 'Pauloh',
                      'age': 32, # 31 in the initial, user got older, updating
                      'email': 'elliot16@mymail.com',
                      'role': 'customer',
                      'phone': '6197021684'}
    resp = app.test_client().put('/users', json=test_user_json)
    assert resp.status_code == 200

def test_user_method_delete():
    resp = app.test_client().delete('/users/2')
    assert resp.status_code == 200

def test_order_method_post():
    test_order_json =  {'id': 1031,
                       'name': 'Сделать домашку',
                       'description': 'Сделать домашку по Фласку-Алхимии в курсе Скайпро',
                       'start_date': '18/12/2022',
                       'end_date': '19/12/2022',
                       'address': 'Не дом и не улица',
                       'price': 0,
                       'customer_id': 24, 'executor_id': 0}
    resp = app.test_client().post('/orders', json=test_order_json)
    assert resp.status_code == 200

def test_order_method_put():
    test_order_json =  {'id': 0,
                        'name': 'Встретить тетю на вокзале',
                        'description': 'Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру',
                        'start_date': '02/08/2013',
                        'end_date': '03/08/2057',
                        'address': '4759 William Haven Apt. 194\nWest Corey, TX 43780',
                        'price': 55120, # price increased x10 - aunt is a nightmare, nobody wants to deal with her
                        'customer_id': 3,
                        'executor_id': 6}
    resp = app.test_client().put('/orders', json=test_order_json)
    assert resp.status_code == 200

def test_order_method_delete():
    resp = app.test_client().delete('/orders/42')
    assert resp.status_code == 200

def test_offer_method_post():
    test_offer_json =  {'id': 1030, 'order_id': 2, 'executor_id': 1}
    resp = app.test_client().post('/offers', json=test_offer_json)
    assert resp.status_code == 200

def test_offer_method_put():
    test_offer_json =  {'id': 0,
                        'order_id': 36,
                        'executor_id': 2 # was 10
                        }
    resp = app.test_client().put('/offers', json=test_offer_json)
    assert resp.status_code == 200

def test_offer_method_delete():
    resp = app.test_client().delete('/offers/1')
    assert resp.status_code == 200