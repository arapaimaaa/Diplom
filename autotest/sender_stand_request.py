import configuration
import requests
import data

def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=body, headers=data.headers)
    return response

def get_order_by_id(id):
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER+str(id))
    return response
