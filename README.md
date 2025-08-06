# 💼 Career Mentor Agent

## 🧠 What It Does

Career Mentor Agent is a multi-agent system designed to guide students through career exploration and planning. It uses multiple specialized agents to recommend personalized career paths, skill roadmaps, and real-world job roles.

### 🔍 Features:
- Recommends career paths based on user interests.
- Uses a tool `get_career_roadmap()` to show the skills needed for a chosen career.
- Switches control between different agents for a smooth user experience.

### 🤖 Agents:
- **CareerAgent** – Suggests relevant career fields based on interests.
- **SkillAgent** – Shows skill-building plans for a selected career.
- **JobAgent** – Provides real-world job roles aligned with the career path.

## ⚙️ Technologies Used:
- **Gemini 2.0 Flash API** (or any compatible API for multi-agent interaction)
- **Multi-Agent Handoff Logic**
- **Tool Integration**:
  - `get_career_roadmap()` – A tool to dynamically fetch skill progression for a given field.

> 🔔 Note: The use of **tools and handoff logic** between agents is an advanced topic not yet covered in class. You are encouraged to independently explore these concepts. They will be discussed in an upcoming session.

## 🚀 How to Run

1. Clone this repository.
2. Add your API key in the `.env` file:
