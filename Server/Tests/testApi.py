import requests


class TestSerch():

    def test_api_login(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myobj = {"email":"dj@mac.com","password":"123456"}
        x = requests.post(url,json=myobj)
        print(x.text)
        assert x.status_code == 200

    def test_api_invalid_login(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myobj = {"email": "d'", "password": "123456"}
        x = requests.post(url, json=myobj)
        print(x.status_code)
        assert x.status_code == 500

    def test_api_register(self):
        url = "https://wetechsocial.herokuapp.com/auth/register"
        myobj ={
                "userName": "asdas",
                "userLastName": "asdas",
                "profilePicture": "sdasd",
                "coverPicture": "https://www.asdasd.com",
                "email": "asas@gmail.com",
                "city": "dj@mac.com",
                "password": "123456",
                "from": "asfd"
                }
        x = requests.post(url,json=myobj)
        print(x.text)
        assert x.status_code == 500



    def test_api_invalid_register(self):
        url = "https://wetechsocial.herokuapp.com/auth/register"
        myobj ={
                "userName": "asdas",
                "userLastName": "asdas",
                "profilePicture": "sdasd",
                "coverPicture": "https://www.asdasd.com",
                "email": "",
                "city": "cd",
                "password": "123456",
                "from": "asfd"
                }
        x = requests.post(url,json=myobj)
        print(x.status_code)
        assert x.status_code == 500