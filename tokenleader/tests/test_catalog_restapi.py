import json
from tokenleader.tests.base_test import  BaseTestCase
from tokenleader.tests.test_catalog_ops import TestCatalog
from tokenleader.tests.test_auth import TestToken
test_token_instance = TestToken()
tc = TestCatalog()

class TestCatalogRestApi(BaseTestCase):
 
    def test_list_services():      
        u1 = tc.list_services()
        with self.client:
            response = self.client.get('/list/services')
            data = json.loads(response.data.decode())
            self.assertTrue(isinstance(data['status'], list))
            
            
           