from .repository import ProductDatabaseRepo, ProductRepo
from .interactors import GetProductInteractor

class ProductDatabaseRepoFactory(object):
    @staticmethod
    def get():
        return ProductDatabaseRepo()

# class ProductCacheRepoFactory(object):
#     @staticmethod
#     def get():
#         return ProductCacheRepo()

class ProductRepoFactory(object):
    @staticmethod
    def get():
        db_repo = ProductDatabaseRepoFactory.get()
        # cache_repo = ProductCacheRepoFactory.get()
        return ProductRepo(db_repo)
    
class GetProductInteractorFactory(object):
    @staticmethod
    def get():
        product_repo = ProductRepoFactory.get()
        return GetProductInteractor(product_repo)

class ProductViewFactory(object):
    @staticmethod
    def create():
        get_product_interactor = GetProductInteractorFactory.get()
        return ProductView(get_product_interactor)