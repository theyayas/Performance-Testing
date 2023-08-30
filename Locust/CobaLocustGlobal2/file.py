from locust import HttpUser, SequentialTaskSet, task, constant


class SeqTask(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/")
        print("home page")

    @task
    def about_page(self):
        self.client.post("/login/", json=
                         {
                             "email" : "yasingammarkanari@gmail.com",
                             "password" : "Password1!"
                         }
                         )
        print("login page")

    @task
    def policy_page(self):
        self.client.get("/absence/checkin/")
        print("check in page")

    '''@task
    def affiliate_page(self):
        self.client.get("/gramedia-affiliate")
        print("affiliate page")

    @task
    def terms_and_condition_page(self):
        self.client.get("/term-and-conditions")
        print("terms and condition page")'''


class Run(HttpUser):
    host = "https://technoapp.berijalan.id"
    tasks = [SeqTask]
    wait_time = constant(1)
