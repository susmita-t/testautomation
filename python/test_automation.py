
import http.client
import json

class TestFixture:
    __instance = None
    __backend = None
    def __init__(self):
        """ Virtually private constructor. """
        if TestFixture.__instance != None:
            raise Exception("Textfixture is a singleton! To get an instance of it, use TestFixture.getInstance() ")
        else:
            TestFixture.__backend = Backend()
            self.fetchdata_service = FetchDataService(TestFixture.__backend)
            TestFixture.__instance = self

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if TestFixture.__instance == None:
            TestFixture()
            return TestFixture.__instance

class Backend:
    def __init__(self):
        #self.host = host
        #self.port = port
        print("Backend")

    def request(self, url, method, path, json_data, header):
        connection = http.client.HTTPSConnection(url)
        connection.request(method, path, json_data, header)
        response = connection.getresponse()
        return response
    
    def get(self, url, path, json_data, header):
        return self.request(url, "GET", path, json_data, header)

    def post(self, url, path, json_data, header):
        return self.request(url, "POST", path, json_data, header)


class FetchDataService:
    def __init__(self, backend):
        self.__backend = backend
        self.__url = "reqres.in"
        self.__header = {'Content-type': 'application/json'}
        print("FetchDataService")

    def get_users(self):
        path_users = "/api/users"
        data = {"page":1}
        json_data = json.dumps(data)
        response = self.__backend.get(self.__url, path_users, json_data, self.__header)
        print_response(response, "SECURED GET")
        json_data = None
        if(response.status == 200):
            str_data = response.read().decode('utf-8')
            json_data = json.loads(str_data)
        return json_data

    def get_user_detail(self, user_id):
        path_users = "/api/users"
        path_user_details = path_users + "/" + user_id
        data = {}
        json_data = json.dumps(data)
        response = self.__backend.get(self.__url, path_user_details, json_data, self.__header)
        print_response(response, "SECURED GET")
        json_data = None
        if(response.status == 200):
            str_data = response.read().decode('utf-8')
            json_data = json.loads(str_data)
        return json_data #json.loads(response.read().decode('utf-8'))['data']
    
    def create_user(self, user_name, job):
        path_user = "/api/users"
        data = {"name": user_name, "job": job}
        json_data = json.dumps(data)
        response = self.__backend.post(self.__url, path_user, json_data, self.__header)
        print_response(response, "SECURED GET")
        json_data = None
        if(response.status == 201):
            str_data = response.read().decode('utf-8')
            json_data = json.loads(str_data)
        return json_data


# TestBase will be derived from Unittest
class TestBase:
    def __init__(self):
        fxt = TestFixture.getInstance()
        self._fetchdata_service = fxt.fetchdata_service
        # frontend will be passed to the respective Page Object
        # The respective page object will return the data loaded in UI
        self._frontend = None
        print("TestBase")

class TestUsers(TestBase):
    def __init__(self):
        TestBase.__init__(self)    
        print("TestUsers")

    def test_users(self):
        users = self._fetchdata_service.get_users()
        # here we will get the number of users from the drop down in the UI 
        # and compare the number of elements in the drop down with the number of users
        # fetched from backend 
        # lets assume the number of users loaded in the frontend drop down are 3
        if(users != None and len(users['data']) == 3):
            print("test_users - SUCCESS")
        else:
            print("test_users - FAILED")
        #print(users)

    def test_user_details(self):        
        # using fetchdata_service, we will find the user with id = '1" and 
        # match the name from the UI
        # first_name should be Janet and last_name should be Weaver
        user_details = self._fetchdata_service.get_user_detail("2")
        if(user_details != None and user_details['data']['first_name'] == "Janet" and user_details['data']['last_name'] == "Weaver"):
            print("test_user_details - SUCCESS")
        else:
            print("test_user_details - FAILED")
        #print(users)
    
    def test_create_user(self):        
        # using fetchdata_service, we will create a new user with name 'Peter' and job 'Leader' 
        # in the frontend, we will see if the new name is added in the drop down list
        # match the name from the UI
        # first_name should be Janet and last_name should be Weaver
        new_user = self._fetchdata_service.create_user("Peter", "Leader")
        if(new_user != None and new_user['name'] == "Peter" and new_user['job'] == "Leader"):
            print("test_user_details - SUCCESS")
        else:
            print("test_user_details - FAILED")
        #print(users)
    

def print_response(response, request_type):
    print('{} {} - a response on a {} request by using "http.client"'.format(
        response.status, response.reason, request_type))
    #content = response.read().decode('utf-8')
    #print(content)

test1 = TestUsers()
test1.test_users()
test1.test_user_details()
test1.test_create_user()

'''

# test GET
users = fetchdata_service.get_users()
print(users)
user_details = fetchdata_service.get_user_detail("1")
print(user_details)

#test POST
new_user_1 = fetchdata_service.create_user("Peter", "Leader")
print(new_user_1)
new_user_2 = fetchdata_service.create_user("Peter", "Leader")
print(new_user_2)

user_details = fetchdata_service.get_user_detail(new_user_2["id"])
print(user_details)

'''
print("END")
