from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

def main():
    print("Welcome to Career Mentor Agent!")
    career_agent = CareerAgent()
    skill_agent = SkillAgent()
    job_agent = JobAgent()

    # Step 1: Get user interests
    interests_input = input("Enter your interests (comma separated, e.g., technology, design): ")
    interests = [i.strip() for i in interests_input.split(",")]

    # CareerAgent suggests careers
    careers = career_agent.suggest_careers(interests)
    print("\nBased on your interests, here are some career paths:")
    for i, career in enumerate(careers, 1):
        print(f"{i}. {career}")

    # User chooses a career
    career_choice = int(input("\nChoose a career by number: "))
    chosen_career = careers[career_choice - 1]
    print(f"\nYou chose: {chosen_career}")

    # SkillAgent shows skill roadmap
    skills = skill_agent.get_skill_roadmap(chosen_career)
    print("\nHere is the skill roadmap for this career:")
    for step in skills:
        print(f"- {step}")

    # Ask if user wants job roles info
    want_jobs = input("\nWould you like to see related job roles? (yes/no): ").strip().lower()
    if want_jobs == "yes":
        jobs = job_agent.get_jobs(chosen_career)
        print("\nRelated job roles:")
        for job in jobs:
            print(f"- {job}")

    print("\nThank you for using Career Mentor Agent!")

if __name__ == "__main__":
    main()
