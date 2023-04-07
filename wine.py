
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Wine:

    def __init__(self):
        cred = credentials.Certificate("access.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    
    def get_all(self): 
        data = self.db.collection('Wine').order_by('id').stream()
        return self.__format_products(data)

    def paginate(self, page=1, limit=10):
        start = limit*page - (limit - 1)
        data = self.db.collection('Wine').order_by('id').start_at({
            'id': start
        }).limit(limit).get()

        return self.__format_products(data)

    def total_products(self):
        data = self.db.collection('Wine').order_by('id').stream()
        products = self.__format_products(data)
        return len(products)

    def __format_products(self, data):
        products = []
        for product in data: 
            products.append(product.to_dict())
        
        return products