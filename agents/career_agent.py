class CareerAgent:
    def __init__(self):
        self.career_fields = [
            "Software Developer",
            "Data Scientist",
            "Product Manager",
            "Graphic Designer"
        ]

    def suggest_careers(self, interests):
        # Simple mapping for demo purposes
        interest_map = {
            "technology": ["Software Developer", "Data Scientist"],
            "business": ["Product Manager"],
            "design": ["Graphic Designer"]
        }
        suggested = []
        for interest in interests:
            suggested.extend(interest_map.get(interest.lower(), []))
        if not suggested:
            suggested = self.career_fields  # fallback all
        return list(set(suggested))
