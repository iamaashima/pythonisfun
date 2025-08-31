import os
import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

GOOGLE_API_KEY = "AIzaSyCr35hxFrpVsbNWgqOwU6PwmkpwLmO2dJA"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Dietary Planner Agent
# Dietary Planner Agent (Updated for clarity and better results)
dietary_planner = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Creates personalized dietary plans based on user input.",
    instructions=[
        "Include all meals: breakfast, lunch, dinner, and snacks.",
        "Follow the user's dietary preference (e.g., Keto, Vegetarian, Low Carb, etc.).",
        "Make sure the plan is aligned with the user's fitness goal (e.g., weight loss, muscle gain).",
        "Provide a full nutritional breakdown: calories, proteins, fats, carbs, vitamins, and minerals.",
        "Add hydration advice (e.g., how much water to drink).",
        "Include tips for easy meal preparation and cooking.",
        "Use web search via DuckDuckGo if more info is needed (e.g., food examples or updated nutrition facts).",
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

def get_meal_plan(age, weight, height, activity_level, dietary_preference, fitness_goal):
    prompt = (f"Create a personalized meal plan for a {age}-year-old person, weighing {weight}kg, "
              f"{height}cm tall, with an activity level of '{activity_level}', following a "
              f"'{dietary_preference}' diet, aiming to achieve '{fitness_goal}'.")
    return dietary_planner.run(prompt)

# Fitness Trainer Agent
fitness_trainer = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Generates customized workout routines based on fitness goals.",
    instructions=[
        "Create a workout plan including warm-ups, main exercises, and cool-downs.",
        "Adjust workouts based on fitness level: Beginner, Intermediate, Advanced.",
        "Consider weight loss, muscle gain, endurance, or flexibility goals.",
        "Provide safety tips and injury prevention advice.",
        "Suggest progress tracking methods for motivation.",
        "If necessary, search the web using DuckDuckGo for additional information.",
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

def get_fitness_plan(age, weight, height, activity_level, fitness_goal):
    prompt = (f"Generate a workout plan for a {age}-year-old person, weighing {weight}kg, "
              f"{height}cm tall, with an activity level of '{activity_level}', "
              f"aiming to achieve '{fitness_goal}'. Include warm-ups, exercises, and cool-downs.")
    return fitness_trainer.run(prompt)

# Team Lead Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.agent import Agent


# Define the Team Lead Agent
team_lead = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Combines diet and workout plans into a holistic health strategy, including a dynamic famous health-related quote.",
    instructions=[
        "Merge personalized diet and fitness plans for a comprehensive approach, Use Tables if possible.",
        "Ensure alignment between diet and exercise for optimal results.",
        "Suggest lifestyle tips for motivation and consistency.",
        "Provide guidance on tracking progress and adjusting plans over time.",
        "Search the web for a famous and inspiring health-related quote and include it with the author's name at the end of the response."
    ],
    tools=[DuckDuckGoTools()],  # Let the model use DuckDuckGo itself
    show_tool_calls=True,
    markdown=True
)

def get_meal_plan(age, weight, height, activity_level, dietary_preference, fitness_goal, allergies):
    return f"Meal plan based on {dietary_preference}, avoiding {', '.join(allergies) if allergies else 'no allergens'}"

def get_fitness_plan(age, weight, height, activity_level, fitness_goal):
    return f"Workout plan for {fitness_goal} at {activity_level} activity level"

# Define the main function to generate the full plan
def get_full_health_plan(name, age, weight, height, activity_level, dietary_preference, fitness_goal, allergies):
    meal_plan = get_meal_plan(age, weight, height, activity_level, dietary_preference, fitness_goal, allergies)
    fitness_plan = get_fitness_plan(age, weight, height, activity_level, fitness_goal)

    prompt = (
        f"Greet the customer, {name}\n\n"
        f"User Information: {age} years old, {weight}kg, {height}cm, activity level: {activity_level}.\n\n"
        f"Fitness Goal: {fitness_goal}\n\n"
        f"Allergies: {', '.join(allergies) if allergies else 'None'}\n\n"
        f"Meal Plan:\n{meal_plan}\n\n"
        f"Workout Plan:\n{fitness_plan}\n\n"
        f"Provide a holistic health strategy integrating both plans. "
        f"At the end, include a famous, inspiring health-related quote with the author."
    )

    return team_lead.run(prompt)  # Replace with `return team_lead.run(prompt)` in production with AI backend


# Streamlit UI setup
st.set_page_config(page_title="AI Health & Fitness Plan", page_icon="🏋️‍♂️", layout="wide")

st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #FF6347;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #4CAF50;
        }
        .sidebar {
            background-color: #F5F5F5;
            padding: 20px;
            border-radius: 10px;
        }
        .content {
            padding: 20px;
            background-color: #E0F7FA;
            border-radius: 10px;
            margin-top: 20px;
        }
        .btn {
            display: inline-block;
            background-color: #FF6347;
            color: white;
            padding: 10px 20px;
            text-align: center;
            border-radius: 5px;
            font-weight: bold;
            text-decoration: none;
            margin-top: 10px;
        }
        .goal-card {
            padding: 20px;
            margin: 10px;
            background-color: #FFF;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle
st.markdown('<h1 class="title">🏋️‍♂️ AI Health & Fitness Plan Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Personalized fitness and nutrition plans to help you achieve your health goals!</p>', unsafe_allow_html=True)

# NEW: Who is this for?
st.markdown("""
<div class="content">
    <h3>🎯 Who Can Use This App?</h3>
    <ul>
        <li><strong>🧑‍💼 Busy Professionals:</strong> Quick and effective meal and workout plans tailored for tight schedules.</li>
        <li><strong>🏃‍♀️ Fitness Enthusiasts:</strong> Structured plans for muscle gain, endurance, and recovery.</li>
        <li><strong>🧘 Beginners:</strong> Easy-to-follow plans for starting a health journey without overwhelm.</li>
        <li><strong>👩‍⚕️ Medically-Conscious Users:</strong> Special diets like Keto or Low Carb for specific health conditions.</li>
        <li><strong>🏡 Stay-at-Home Parents:</strong> Home-friendly workouts and budget-conscious meals.</li>
        <li><strong>🏕️ Frequent Travelers:</strong> Minimal-equipment fitness routines and portable meal suggestions.</li>
        <li><strong>🎯 Goal-Focused Individuals:</strong> Whether for weight loss, muscle gain, or flexibility—this tool adapts.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("⚙️ Health & Fitness Inputs")
st.sidebar.subheader("Personalize Your Fitness Plan")

age = st.sidebar.number_input("Age (in years)", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
activity_level = st.sidebar.selectbox("Activity Level", ["Low", "Moderate", "High"])
dietary_preference = st.sidebar.selectbox("Dietary Preference", [
    "Keto", "Vegetarian", "Low-carbohydrate", "Balanced", "Diabetes", "Dairy-free"
])
fitness_goal = st.sidebar.selectbox("Fitness Goal", [
    "Weight Loss", "Muscle Gain", "Endurance", "Flexibility"
])

# ✅ New: Food Allergy Input
allergies = st.sidebar.multiselect(
    "Food Allergies (select all that apply)",
    ["Wheat", "Nuts", "Fish", "Shellfish", "Eggs", "Soy"],
    help="Choose any food allergies you have to tailor your meal plan."
)

st.markdown("---")

# Personal Info
st.markdown("### 🏃‍♂️ Personal Fitness Profile")
name = st.text_input("What's your name?", "John Doe")

# Generate Plan
if st.sidebar.button("Generate Health Plan"):
    if not age or not weight or not height:
        st.sidebar.warning("Please fill in all required fields.")
    else:
        with st.spinner("💥 Generating your personalized health & fitness plan..."):
            full_health_plan = get_full_health_plan(name, age, weight, height, activity_level, dietary_preference, fitness_goal)
        
            st.subheader("Your Personalized Health & Fitness Plan")
            st.markdown(full_health_plan.content)
            st.info("This is your customized health and fitness strategy, including meal and workout plans.")

        st.markdown("""
            <div class="goal-card">
                <h4>🏆 Stay Focused, Stay Fit!</h4>
                <p>Consistency is key! Keep pushing yourself, and you will see results. Your fitness journey starts now!</p>
            </div>
        """, unsafe_allow_html=True)
