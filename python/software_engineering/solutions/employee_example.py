class Employee:

    def __init__(self, name, job_title, job_location):
        self.name = name
        self.job_title = job_title
        self.job_location = job_location

    def greeting(self):
        return f"Hello, my name is {self.name} and I am a {self.job_title}"

    def estimated_salary(self):
        if self.job_title == "Software Engineer":
            if self.job_location == "San Francisco":
                return "150K"
            elif self.location == "Dallas":
                return "90K"
            else:
                return "70K"
        else:
            return "40K"


jamie = Employee("Jamie", "Software Engineer", "San Francisco")
print(jamie.greeting())
print("Jamie's salary is", jamie.estimated_salary())
