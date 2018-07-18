from pricing_service.api.models import Product

def test_new_product(new_product):
  assert new_product.price == 250
  assert new_product.name == 'Pedigree Chum Mixir'
  assert new_product.sku == 'PED'
