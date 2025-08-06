from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

def main():
    print("Welcome to Career Mentor Agent!\n")

    interests = input("What are your interests? (e.g., technology, art, business): ").lower()

    career_agent = CareerAgent()
    print("\nSuggested Career Paths:")
    careers = career_agent.suggest_careers(interests)
    print(careers)

    selected_career = input("\nEnter one career from above that interests you: ").strip()

    skill_agent = SkillAgent()
    print(f"\nSkill Roadmap for {selected_career}:")
    roadmap = skill_agent.show_skills(selected_career)
    print(roadmap)

    job_agent = JobAgent()
    print(f"\nReal-World Job Roles in {selected_career}:")
    jobs = job_agent.show_job_roles(selected_career)
    print(jobs)

if __name__ == "__main__":
    main()
