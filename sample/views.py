import json

from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from .factories import GetProductInteractorFactory
from .serializers import ProductSerializer

class ViewWrapper(View):
    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)

        return HttpResponse(json.dumps(body), status=status,content_type='application/json')

class ProductView(object):
    def __init__(self, get_product_interactor):
        self.get_product_interactor = get_product_interactor
    
    def get(self, reference):
        try:
            product = self.get_product_interactor.set_params(reference=reference).execute()
        except ValueError:
            body = {'error': 'Product does not exist!'}
            status = 404
        else:
            body = ProductSerializer.serialize(product)
            status = 200
        
        return body, status
        