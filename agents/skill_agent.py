from gemini import ask_gemini

class SkillAgent:
    def show_skills(self, career):
        prompt = f"""
        I have chosen the career '{career}'.
        Can you give me a skill-building roadmap to succeed in this field?
        Return it as a step-by-step list.
        """
        return ask_gemini(prompt)
