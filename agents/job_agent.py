from gemini import ask_gemini

class JobAgent:
    def show_job_roles(self, career):
        prompt = f"""
        What are some real-world job titles or roles available in the career path '{career}'?
        List them in bullet points.
        """
        return ask_gemini(prompt)
