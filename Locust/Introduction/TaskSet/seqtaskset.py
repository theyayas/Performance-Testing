from locust import SequentialTaskSet, HttpUser, task, constant


class SeqTask(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/")
        print("home page")

    @task
    def get_mobil_baru(self):
        self.client.get("/mobil - baru")
        print("mobil baru")

    @task
    def get_promo(self):
        self.client.get("/info/promo/")
        print("promo")

    @task
    def get_artikel(self):
        self.client.get("/blog/category/otomotif/")
        print("artikel")

    @task
    def get_about(self):
        self.client.get("/info/tentang-kami/")
        print("about page")


class Run(HttpUser):
    host = "https://www.seva.id"
    tasks = [SeqTask]
    wait_time = constant(1)
