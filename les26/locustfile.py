from locust import HttpUser, task, constant


class MyFirstUser(HttpUser):
    wait_time = constant(1)

    @task
    def my_task(self):
        self.client.get("/pet/findByStatus?status=sold")
