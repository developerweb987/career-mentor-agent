def get_career_roadmap(career):
    roadmaps = {
        "software developer": [
            "Learn programming basics (Python, Java, or JavaScript)",
            "Understand data structures and algorithms",
            "Build small projects",
            "Learn version control with Git",
            "Explore web development or app development frameworks",
            "Practice coding interviews"
        ],
        "data scientist": [
            "Learn Python and statistics",
            "Understand data cleaning and preprocessing",
            "Master machine learning basics",
            "Work on data visualization",
            "Learn SQL and databases",
            "Build real-world projects"
        ],
        "product manager": [
            "Understand product lifecycle",
            "Learn Agile and Scrum methodologies",
            "Improve communication and leadership skills",
            "Learn to write product requirement documents",
            "Familiarize with UX/UI basics",
            "Get hands-on experience in product delivery"
        ],
        "graphic designer": [
            "Master design tools like Adobe Photoshop and Illustrator",
            "Learn design principles and color theory",
            "Practice creating logos, banners, and mockups",
            "Build a portfolio",
            "Understand branding basics",
            "Stay updated with design trends"
        ],
        # Add more career fields as needed
    }
    career = career.lower()
    return roadmaps.get(career, ["Sorry, no roadmap found for this career."])
