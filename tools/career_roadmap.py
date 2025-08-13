def get_career_roadmap(field):
    roadmap = {
        "Data Science": ["Python", "Statistics", "Machine Learning", "Data Visualization"],
        "Web Development": ["HTML", "CSS", "JavaScript", "React", "Backend Frameworks"],
        "Cybersecurity": ["Networking", "Linux", "Penetration Testing", "Security Protocols"]
    }
    return roadmap.get(field, ["No roadmap available for this field"])
