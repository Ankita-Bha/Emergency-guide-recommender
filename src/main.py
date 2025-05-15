"""import streamlit as st
import pandas as pd
import recommender
import chatbot

# File path
file_path = "../data/dataset.csv"

# Try to load the dataset
try:
    df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
except Exception as e:
    st.error(f"❌ Dataset format issue: {str(e)}")
    df = pd.DataFrame(columns=["Emergency Type", "Description", "Possible Complications", "Immediate Response", "Resource Links"])

# Streamlit UI
st.title("🚑 Medical Emergency Assistance")

st.header("🩺 Common Medical Emergencies")
if df.empty:
    st.warning("⚠️ No emergency data available.")
else:
    for _, row in df.iterrows():
        with st.expander(f"⚠️ {row['Emergency Type']}"):
            st.write(f"**Description:** {row['Description']}")
            st.write(f"**Possible Complications:** {row['Possible Complications']}")
            st.write(f"**Immediate Response:** {row['Immediate Response']}")
            if pd.notna(row['Resource Links']):
                st.write(f"[More Info]({row['Resource Links']})")

# 📝 User Input Form
st.sidebar.header("📝 Enter Your Details")
name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", min_value=0, max_value=120)
hobbies = st.sidebar.text_area("Hobbies")
usual_places = st.sidebar.text_area("Places you frequently visit")
parent_medical_history = st.sidebar.text_area("Parent's Medical History")

# 🧠 Risk Analysis Feature
if st.sidebar.button("Analyze My Risks"):
    user_data = {
        "hobbies": hobbies or "",
        "parent_medical_history": parent_medical_history or ""
    }
    risks = recommender.analyze_risks(user_data)  # Calling the function from recommender.py
    
    st.sidebar.subheader("⚠️ Personalized Risk Analysis")
    if risks:
        for risk in risks:
            st.sidebar.write(f"🔴 {risk}")
    else:
        st.sidebar.write("✅ No major risks detected.")"""

# import streamlit as st
# import pandas as pd
# import recommender

# # File path
# file_path = "../data/dataset.csv"

# # Try to load the dataset
# try:
#     df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
# except Exception as e:
#     st.error(f"❌ Dataset format issue: {str(e)}")
#     df = pd.DataFrame(columns=["Emergency Type", "Description", "Possible Complications", "Immediate Response", "Resource Links"])

# # Streamlit UI
# st.title("🚑 Medical Emergency Assistance")

# # User Input Form
# st.sidebar.header("📝 Enter Your Details")
# user_name = st.sidebar.text_input("Name")
# user_age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
# user_hobbies = st.sidebar.text_area("Hobbies")
# user_parent_medical_history = st.sidebar.text_area("Parental Medical History")

# # Analyzing risks based on user input
# if st.sidebar.button("Analyze Risks"):
#     user_data = {
#         "hobbies": user_hobbies,
#         "parent_medical_history": user_parent_medical_history
#     }
#     risks = recommender.analyze_risks(user_data)
#     if risks:
#         st.sidebar.warning("⚠️ Identified Risks:")
#         for risk in risks:
#             st.sidebar.write(f"🔹 {risk}")
#     else:
#         st.sidebar.success("✅ No significant risks detected.")

# # Medical Emergencies Section
# st.header("🩺 Common Medical Emergencies")
# if df.empty:
#     st.warning("⚠️ No emergency data available.")
# else:
#     emoji_map = {
#         "Heart Attack": "💔",
#         "Stroke": "🧠",
#         "Fracture": "🦴",
#         "Heatstroke": "🌞",
#         "Choking": "🤧",
#         "Fainting": "😵",
#         "Burns": "🔥",
#         "Severe Bleeding": "🩸",
#         "Asthma Attack": "😤",
#         "Allergic Reaction": "🤧",
#     }

#     for _, row in df.iterrows():
#         emergency_type = row['Emergency Type']
#         emoji = emoji_map.get(emergency_type, "⚠️")  # Default to ⚠️ if not found

#         # Square card structure
#         with st.container():
#             st.markdown(
#                 f"""
#                 <div style="
#                     border: 2px solid #444;
#                     padding: 15px;
#                     border-radius: 12px;
#                     background-color: #1e1e1e;
#                     box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
#                     text-align: center;
#                     margin-bottom: 10px;
#                 ">
#                     <h3 style="color: #ffcc00;">{emoji} {emergency_type}</h3>
#                     <details>
#                         <summary style="cursor: pointer; color: #ddd; font-weight: bold;">Click for details</summary>
#                         <p style="color: #ddd;"><strong>Description:</strong> {row['Description']}</p>
#                         <p style="color: #ddd;"><strong>Complications:</strong> {row['Possible Complications']}</p>
#                         <p style="color: #ddd;"><strong>Immediate Response:</strong> {row['Immediate Response']}</p>
#                         {'<a href="'+row["Resource Links"]+'" style="color: cyan;">More Info</a>' if pd.notna(row['Resource Links']) else ""}
#                     </details>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

# import streamlit as st
# import pandas as pd
# import recommender
# import google.generativeai as genai  # Gemini AI

# # Configure Streamlit for better mobile view
# st.set_page_config(page_title="Medical Emergency Assistance", layout="wide")

# # Set up Gemini AI
# genai.configure(api_key="AIzaSyBrBumiKemumu_S4uAC98wmrhTNdPqX4tE")  # Replace with your API key
# model = genai.GenerativeModel("gemini-pro")

# # File path
# file_path = "../data/dataset.csv"

# # Load the dataset
# try:
#     df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
# except Exception as e:
#     st.error(f"❌ Dataset format issue: {str(e)}")
#     df = pd.DataFrame(columns=["Emergency Type", "Description", "Possible Complications", "Immediate Response", "Resource Links"])

# # Main UI
# st.title("🚑 Medical Emergency Assistance")

# # Display GIF
# #st.image("emergency.gif", use_column_width=True)  # Replace with your GIF file

# # Tabs for Main Features
# tab1, tab2 = st.tabs(["🏥 Emergency Info", "🤖 AI Chatbot"])

# # ✅ Tab 1: Emergency Information
# with tab1:
#     st.sidebar.header("📝 Enter Your Details")
#     user_name = st.sidebar.text_input("Name")
#     user_age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
#     user_hobbies = st.sidebar.text_area("Hobbies")
#     user_parent_medical_history = st.sidebar.text_area("Parental Medical History")

#     # Analyze risks
#     if st.sidebar.button("Analyze Risks"):
#         user_data = {"hobbies": user_hobbies, "parent_medical_history": user_parent_medical_history}
#         risks = recommender.analyze_risks(user_data)
#         if risks:
#             st.sidebar.warning("⚠️ Identified Risks:")
#             for risk in risks:
#                 st.sidebar.write(f"🔹 {risk}")
#         else:
#             st.sidebar.success("✅ No significant risks detected.")

#     # Medical Emergencies Section
#     st.header("🩺 Common Medical Emergencies")
#     if df.empty:
#         st.warning("⚠️ No emergency data available.")
#     else:
#         emoji_map = {
#             "Heart Attack": "💔", "Stroke": "🧠", "Fracture": "🦴", "Heatstroke": "🌞",
#             "Choking": "🤧", "Fainting": "😵", "Burns": "🔥", "Severe Bleeding": "🩸",
#             "Asthma Attack": "😤", "Allergic Reaction": "🤧",
#         }

#         for _, row in df.iterrows():
#             emergency_type = row['Emergency Type']
#             emoji = emoji_map.get(emergency_type, "⚠️")

#             with st.container():
#                 st.markdown(
#                     f"""
#                     <div style="
#                         border: 2px solid #444;
#                         padding: 15px;
#                         border-radius: 12px;
#                         background-color: #1e1e1e;
#                         box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
#                         text-align: center;
#                         margin-bottom: 10px;
#                     ">
#                         <h3 style="color: #ffcc00;">{emoji} {emergency_type}</h3>
#                         <details>
#                             <summary style="cursor: pointer; color: #ddd; font-weight: bold;">Click for details</summary>
#                             <p style="color: #ddd;"><strong>Description:</strong> {row['Description']}</p>
#                             <p style="color: #ddd;"><strong>Complications:</strong> {row['Possible Complications']}</p>
#                             <p style="color: #ddd;"><strong>Immediate Response:</strong> {row['Immediate Response']}</p>
#                             {'<a href="'+row["Resource Links"]+'" style="color: cyan;">More Info</a>' if pd.notna(row['Resource Links']) else ""}
#                         </details>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

# # ✅ Tab 2: AI Chatbot
# with tab2:
#     st.header("🤖 Ask the AI Assistant")
#     user_query = st.text_area("Ask about medical emergencies:")
    
#     if st.button("Get Answer"):
#         if user_query.strip():
#             with st.spinner("Thinking..."):
#                 response = model.generate_content(user_query)
#                 st.success("✅ AI Response:")
#                 st.write(response.text)
#         else:
#             st.warning("⚠️ Please enter a question.")

# # ✅ Mobile Responsiveness
# st.markdown(
#     """
#     <style>
#         [data-testid="stAppViewContainer"] {
#             max-width: 100%;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# import streamlit as st
# import pandas as pd
# import google.generativeai as genai  # Gemini AI
# import recommender  # Custom module for risk analysis

# # 🔥 ENTER YOUR GEMINI API KEY HERE
# API_KEY = "AIzaSyDmiYGG2-6a1wPS035QOuEfujJfSOLxxDM"  # Replace this with your actual API key

# # Configure Streamlit
# st.set_page_config(page_title="Medical Emergency Assistance", layout="wide")

# # Validate API key
# if not API_KEY or API_KEY.startswith("YOUR"):
#     st.error("❌ Please enter a valid Gemini API key in the script.")
# else:
#     # Set up Gemini AI
#     genai.configure(api_key=API_KEY)

#     # Load available models
#     try:
#         available_models = [m.name for m in genai.list_models()]
#         model_name = "gemini-pro" if "gemini-pro" in available_models else available_models[0]
#         model = genai.GenerativeModel(model_name)
#     except Exception as e:
#         st.error(f"❌ Error loading Gemini AI: {str(e)}")
#         model = None  # Prevent crashes

# # Load dataset (fallback to empty DataFrame if missing)
# file_path = "../data/dataset.csv"
# try:
#     df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
# except Exception as e:
#     st.warning(f"⚠️ Could not load dataset: {str(e)}")
#     df = pd.DataFrame(columns=["Emergency Type", "Description", "Possible Complications", "Immediate Response", "Resource Links"])

# # Main UI
# st.title("🚑 Medical Emergency Assistance")

# # Tabs for features
# tab1, tab2 = st.tabs(["🏥 Emergency Info", "🤖 AI Chatbot"])

# # Tab 1: Emergency Information
# with tab1:
#     st.sidebar.header("📝 Enter Your Details")
#     user_name = st.sidebar.text_input("Name")
#     user_age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
#     user_hobbies = st.sidebar.text_area("Hobbies")
#     user_parent_medical_history = st.sidebar.text_area("Parental Medical History")

#     # Analyze risks
#     if st.sidebar.button("Analyze Risks"):
#         user_data = {"hobbies": user_hobbies, "parent_medical_history": user_parent_medical_history}
#         risks = recommender.analyze_risks(user_data)
#         if risks:
#             st.sidebar.warning("⚠️ Identified Risks:")
#             for risk in risks:
#                 st.sidebar.write(f"🔹 {risk}")
#         else:
#             st.sidebar.success("✅ No significant risks detected.")

#     # Medical Emergencies Section
#     st.header("🩺 Common Medical Emergencies")
#     if df.empty:
#         st.warning("⚠️ No emergency data available.")
#     else:
#         for _, row in df.iterrows():
#             emergency_type = row['Emergency Type']
#             with st.expander(f"🚨 {emergency_type}"):
#                 st.write(f"**Description:** {row['Description']}")
#                 st.write(f"**Complications:** {row['Possible Complications']}")
#                 st.write(f"**Immediate Response:** {row['Immediate Response']}")
#                 if pd.notna(row['Resource Links']):
#                     st.markdown(f"[More Info]({row['Resource Links']})")

# # Tab 2: AI Chatbot
# with tab2:
#     st.header("🤖 Ask the AI Assistant")
#     user_query = st.text_area("Ask about medical emergencies:")

#     if st.button("Get Answer"):
#         if user_query.strip():
#             if model:
#                 with st.spinner("Thinking..."):
#                     try:
#                         response = model.generate_content(user_query)
#                         st.success("✅ AI Response:")
#                         st.write(response.text)
#                     except Exception as e:
#                         st.error(f"❌ Error generating response: {str(e)}")
#             else:
#                 st.error("❌ AI model failed to load. Please check your API key.")
#         else:
#             st.warning("⚠️ Please enter a question.")

# # Mobile Responsiveness
# st.markdown(
#     """
#     <style>
#         [data-testid="stAppViewContainer"] {
#             max-width: 100%;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
import pandas as pd
import google.generativeai as genai  # Gemini AI

# ✅ Enter Your Gemini API Key
API_KEY = "AIzaSyAJZLxr9aoFRCWrh_0JXU-abaWYSyHjFnA"  # Replace with your actual API key

# ✅ Configure Gemini AI
if not API_KEY:
    st.error("❌ Please enter a valid Gemini API key in the script.")
else:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-pro")  # Using Gemini 1.5 Pro
    except Exception as e:
        st.error(f"❌ Error initializing Gemini AI: {str(e)}")
        model = None  # Prevents crashes

# ✅ Load Dataset
file_path = "dataset.csv"  # Ensure dataset.csv is in the same folder
try:
    df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
except Exception as e:
    st.warning(f"⚠️ Could not load dataset: {str(e)}")
    df = pd.DataFrame(columns=["Emergency Type", "Description", "Possible Complications", "Immediate Response", "Resource Links"])

# ✅ Streamlit UI
st.set_page_config(page_title="Medical Emergency Assistance", layout="wide")
st.title("🚑 Medical Emergency Assistance")

# ✅ Tabs for Features
tab1, tab2 = st.tabs(["🏥 Emergency Info", "🤖 AI Chatbot"])

# 📌 **Emergency Information**
with tab1:
    st.sidebar.header("📝 Enter Your Details")
    user_name = st.sidebar.text_input("Name")
    user_age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
    user_hobbies = st.sidebar.text_area("Hobbies")
    user_parent_medical_history = st.sidebar.text_area("Parental Medical History")

    if st.sidebar.button("Analyze Risks"):
        if "heart" in user_parent_medical_history.lower():
            st.sidebar.warning("⚠️ Risk of cardiovascular issues detected!")
        else:
            st.sidebar.success("✅ No significant risks detected.")

    st.header("🩺 Common Medical Emergencies")
    if df.empty:
        st.warning("⚠️ No emergency data available.")
    else:
        for _, row in df.iterrows():
            with st.expander(f"🚨 {row['Emergency Type']}"):
                st.write(f"**Description:** {row['Description']}")
                st.write(f"**Complications:** {row['Possible Complications']}")
                st.write(f"**Immediate Response:** {row['Immediate Response']}")
                if pd.notna(row['Resource Links']):
                    st.markdown(f"[More Info]({row['Resource Links']})")

# 🧠 **AI Chatbot**
with tab2:
    st.header("🤖 Ask the AI Assistant")
    user_query = st.text_area("Ask about medical emergencies:")

    if st.button("Get Answer"):
        if user_query.strip():
            if model:
                with st.spinner("Thinking..."):
                    try:
                        response = model.generate_content(user_query)
                        st.success("✅ AI Response:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"❌ Error generating response: {str(e)}")
            else:
                st.error("❌ AI model failed to load. Please check your API key.")
        else:
            st.warning("⚠️ Please enter a question.")

# ✅ Mobile Responsiveness Fix
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            max-width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)
