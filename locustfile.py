from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task
    def query(self):
        self.client.get("/arama?q=iphone")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
