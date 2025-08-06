from gemini import ask_gemini

class CareerAgent:
    def suggest_careers(self, interests):
        prompt = f"""
        I am a student with interests in {interests}.
        Please suggest 3 to 5 career paths I can explore.
        Return them as a bullet point list.
        """
        return ask_gemini(prompt)
