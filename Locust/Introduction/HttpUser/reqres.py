from locust import HttpUser, task, constant


class MyReqTest(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)  # in second

    @task
    def get_user(self):
        # sesuaikan dengan http method (dalam kasus ini GET)
        self.client.get("/api/users?page=2")  # masukkan path di sini

    @task
    def create_user(self):
        self.client.post("/api/users", data='''
        {name: "morpheus", job: "leader"}
        ''')
