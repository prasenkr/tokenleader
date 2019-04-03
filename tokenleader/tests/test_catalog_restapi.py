import json
from tokenleader.tests.base_test import  BaseTestCase
from tokenleader.tests.test_catalog_ops import TestCatalog
from tokenleader.tests.test_auth import TestToken
test_token_instance = TestToken()
t = TestCatalog()

class TestCatalogRestApi(BaseTestCase):
 
    def test_list_services_restapi(self):      
        u1 = t.list_services()
        with self.client:
            response = self.client.get('/list/service/tokenleader')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'].get('name') == 'tokenleader')
            
            
 
    def test_add_service_restapi(self):
        u1 = t.add_service()
#         t.register_work_function_for_test()
        data = json.dumps(dict(
            name = 'tokenleader',
            pwd = 'password',
            urlint = 'localhost:5005',
            urlext= 'localhost:5005',
            urladmin = 'localhost:5005',
            ))
        print(data)
        with self.client:
            response = self.client.post(
                '/add/service',
                data=data,
                content_type='application/json')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'tokenleader has been registered.')     
    
    
 