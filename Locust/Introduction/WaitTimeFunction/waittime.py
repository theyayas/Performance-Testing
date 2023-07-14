from locust import SequentialTaskSet, task, constant, User
import time


class SeqTest(SequentialTaskSet):

    @task
    def first(self):
        print("first")
        # time.sleep(1)

    @task
    def second(self):
        print("second")
        # time.sleep(1)

class Run(User):
    tasks = [SeqTest]
    wait_time = constant(1)
