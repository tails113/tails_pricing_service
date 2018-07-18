import pytest

from pricing_service import (db, create_app)

from pricing_service.api.models import Product, VATBand

@pytest.fixture(scope='module')
def new_product():
    vat = VATBand(name='standard',
                  rate=0.2)
    product = Product(sku='PED',
		      name='Pedigree Chum Mixir',
                      price=250,
                      vatband=vat)
    return product


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='module')
def create_products(init_database, new_product):
    init_database.session.add(new_product)
    init_database.session.commit()
