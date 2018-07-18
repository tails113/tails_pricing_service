import json


def test_single_product(test_client, init_database, create_products):
    data = {"order": {
	        "id": 1,
		"customer": {},
		"items": [ { "product_id": 1,
			     "quantity": 1 } ]
	    }
     }
    response = test_client.post('/api/products',
		                data=json.dumps(data),
                                headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    import pdb; pdb.set_trace()
    assert response.json['prices']
