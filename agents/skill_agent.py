from tools.skill_tools import get_career_roadmap

class SkillAgent:
    def get_skill_roadmap(self, career):
        roadmap = get_career_roadmap(career)
        return roadmap
