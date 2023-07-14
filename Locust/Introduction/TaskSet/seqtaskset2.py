from locust import HttpUser, SequentialTaskSet, task, constant


class MyScript(SequentialTaskSet):

    @task(1)
    def home_page(self):
        with self.client.get("/") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("home gagal")

    @task(2)
    def policy(self):
        with self.client.get("/mobil - baru") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("policy gagal")


class Run(HttpUser):
    host = "https://www.seva.id"
    tasks = [MyScript]
    wait_time = constant(1)

