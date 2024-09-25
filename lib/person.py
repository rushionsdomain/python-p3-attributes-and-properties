class Person:
    approved_jobs = ["Sales", "ITC", "Engineering"]

    def __init__(self, name="", job=""):
        """Initializes a Person instance with a name and a job."""
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self.name = name.title()
        
        if job not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
            return
        self.job = job
