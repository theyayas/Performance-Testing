from locust import TaskSet, task, constant, HttpUser
import random


class CobaTaskSet(TaskSet):  # tidak bisa berjalan dengan sendirinya, harus dipanggil di HttpUser

    '''@task
    def get_status(self):
        self.client.get("/200")
        print("Get status code 200")'''

    '''@task
    def get_random_status(self):
        random_code = random.randint(100,400)
        self.client.get("/" + str(random_code))
        print("Get random status code")'''

    @task
    def get_random_status2(self):
        random_code2 = [100, 101, 102, 103,
                        200, 201, 202, 203, 204, 206, 207,
                        300, 301, 302, 303, 304, 305, 307, 308,
                        400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410,
                        411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422,
                        423, 424, 425, 426, 429, 431, 444, 450, 451, 497, 498,
                        499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510,
                        511, 521, 522, 523, 525, 599]
        get_code = "/" + str(random.choice(random_code2))
        self.client.get(get_code)


class RunHttpUser(HttpUser):
    host = "https://http.cat"
    tasks = [CobaTaskSet] # tasks : memanggil class CobaTaskSet
    wait_time = constant(1)
