import data
import sender_stand_request

def test_create_order_success_response():
    create_order_response = sender_stand_request.post_new_order(data.create_order_body)
    assert create_order_response.status_code == 201
    get_order_response = sender_stand_request.get_order_by_id(create_order_response.json()["track"])
    assert get_order_response.status_code == 200

print(test_create_order_success_response())



