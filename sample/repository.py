from .models import ORMProduct
from .entities import Product

class ProductDatabaseRepo(object):
    def get_product(self, reference):
        try:
            orm_product = ORMProduct.objects.get(reference=reference)
        
        except ORMProduct.DoesNotExist:
            raise ValueError()
    
    def _decode_orm_product(self, orm_product):
        return Product(reference=orm_product.reference, brand_id=orm_product.brand_id)