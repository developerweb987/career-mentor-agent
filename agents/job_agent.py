class JobAgent:
    def __init__(self):
        self.job_roles = {
            "software developer": [
                "Frontend Developer",
                "Backend Developer",
                "Full Stack Developer",
                "Mobile App Developer"
            ],
            "data scientist": [
                "Data Analyst",
                "Machine Learning Engineer",
                "Data Engineer"
            ],
            "product manager": [
                "Associate Product Manager",
                "Technical Product Manager",
                "Product Owner"
            ],
            "graphic designer": [
                "Brand Designer",
                "UX Designer",
                "Visual Designer"
            ],
        }

    def get_jobs(self, career):
        career = career.lower()
        return self.job_roles.get(career, ["No jobs found for this career."])
