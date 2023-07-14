from locust import HttpUser, SequentialTaskSet, task, constant


class SeqTask(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/")
        print("home page")

    @task
    def about_page(self):
        self.client.get("/about/")
        print("about page")

    @task
    def policy_page(self):
        self.client.get("/shopping-policy")
        print("policy page")

    @task
    def affiliate_page(self):
        self.client.get("/gramedia-affiliate")
        print("affiliate page")

    @task
    def terms_and_condition_page(self):
        self.client.get("/term-and-conditions")
        print("terms and condition page")


class Run(HttpUser):
    host = "https://www.gramedia.com"
    tasks = [SeqTask]
    wait_time = constant(1)
