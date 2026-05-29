from locust import HttpUser, task, between


class TravelUser(HttpUser):

    wait_time = between(1, 2)

    @task
    def get_airports(self):

        self.client.get("/airports")


    @task
    def get_airport_by_id(self):

        self.client.get("/airports/1")