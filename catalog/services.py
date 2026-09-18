from django.core.cache import cache
from django.db.models.query_utils import select_related_descend
from select import select
from unicodedata import category

from .models import Category, Product

class ProductService:

    @staticmethod
    def product_get_by_category(category_id):
        cache_key = f"category_{category_id}_products"
        products = cache.get(cache_key)

        if products is None:
            products = list(Product.objects.filter(category_id=category_id))

            cache.set(cache_key, products, 60 * 1)
        return products