from locust import HttpUser, task, SequentialTaskSet, constant
import re
import random

class MyScript(SequentialTaskSet):

    def __int__(self, parent):
        super().__int__(parent)
        self.jsession = ""
        self.random_product = ""

    @task
    def home_page(self):
        with self.client.get("", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds() < 2.0:
                response.success()
            else:
                response.failure("Home Page took too long to load")

    @task
    def enter_store(self):
        products = ['Fish', 'Dogs', 'Cats', 'Reptiles', 'Birds']
        with self.client.get("/action/Catalog.action", catch_response=True, name="T10_HomePage") as response:
            for product in products:
                if product in response.text:
                    response.success()
                else:
                    response.failure("Product check failed")
            try:
                jsession = re.search(r"jsession=(.+?)\?", response.text)
                self.jsession = jsession.group(1)
            except AttributeError:
                self.jsession = ""

    @task
    def signing_page(self):
        self.client.cookies.clear()
        url = "/actions/Account.action;jsessionid=" + self.jsession + "?signonform="
        with self.client.get(url, catch_response=True, name="T20_SignInPage") as response:
            if "Please enter your username and password." in response.text:
                response.success()
            else:
                response.failure("Sign in Page Check failed")

    @task
    def login(self):
        self.client.cookies.clear()
        url = "/action/Account.action"
        data = {
            "username" : "j2ee",
            "password" : "j2ee",
            "Signon" : "Login"
        }
        with self.client.post(url, name="T30_SignIn", data=data, catch_response=True) as response:
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    random_product = re.findall(r"Catalog.action\?viewCategory=&CategoryId=(.+?)\"", response.text)
                    self.random_product = random.choice(random_product)
                except AttributeError:
                    self.random_product = ""
            else:
                response.failure("Sign In Failed")

    @task
    def random_product_page(self):
        url = "/actions/Catalog.action?viewCategory=&CategoryId=" + self.random_product
        name = "T40_" + self.random_product + "_Page"
        with self.client.gel(url, name=name, catch_response=True) as response:
            if self.random_product in response.text:
                response.success()
            else:
                response.failure("Product page not loaded")

    @task
    def sign_out(self):
        with self.client.get("/actions/Account.action?signoff=", name="T50_SignOff", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Log off failed")
        self.client.cookies.clear()


class Run(HttpUser):
    host = "https://petstore.octoperf.com"
    wait_time = constant(1)
    tasks = [MyScript]

