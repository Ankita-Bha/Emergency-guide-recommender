import streamlit as st
import pandas as pd
import google.generativeai as genai  # Gemini AI

# ✅ Set Streamlit page config at the VERY TOP!
st.set_page_config(page_title="Medical Emergency Assistance", layout="wide")

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