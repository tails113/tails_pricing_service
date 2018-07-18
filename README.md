# Pricing Service Test for tails.com

## Installing the requirements
virtualenv --python=python3 env
source env/bin/active
pip install -r requirements.txt

## Running the server
To tun the server use the following command:
python run.py


## Calling the API
With the server running you can the call the API:
http://127.0.0.1:8000/api/products

'''json
{
    "order": {
	"id": 12345,
	"customer": {},
	"items": [
	    {
		"product_id": 1,
		"quantity": 1
	    },
	    {
		"product_id": 2,
		"quantity": 5
	    }
	]
    }
}
'''

## Adding more product and VATBands
If you want to add more products and VATBands, they can be added through the flask shell. 
export FLASK_APP=run.py
flask shell
