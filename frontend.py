# import streamlit as st
# import requests

# st.set_page_config(page_title="AI Multi-Tool", layout="centered")
# st.title("🧠 AI Chatbot • Transcriber • Moderator")

# # 🚀 Step 1: Task Type Selection
# task_type = st.selectbox("Choose Task Type:", ["chat", "transcription", "moderation"])

# # ✍️ Common Inputs
# system_prompt = st.text_area("System Prompt:", height=150, placeholder="E.g. You are a helpful assistant.")
# provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

# MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama3-70b-8192"]
# MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# # 🔘 Model Selector
# selected_model = st.selectbox(
#     "Select Model:",
#     MODEL_NAMES_GROQ if provider == "Groq" else MODEL_NAMES_OPENAI
# )

# # 🔍 Web search toggle (only for chat)
# allow_search = st.checkbox("Enable Web Search") if task_type == "chat" else False

# # 💬 For Chat & Moderation
# if task_type in ["chat", "moderation"]:
#     user_input = st.text_area("Enter your input:", height=150, placeholder="Type your query or text to moderate")
# else:
#     user_input = "Transcription feature coming soon."  # Placeholder

# # 🟢 Backend URL
# API_URL = "http://127.0.0.1:9999/chat"

# # 🚀 Run Task
# if st.button("Run Task"):
#     if user_input.strip() or task_type == "transcription":
#         payload = {
#             "task_type": task_type,
#             "model_name": selected_model,
#             "model_provider": provider,
#             "system_prompt": system_prompt,
#             "messages": [user_input],
#             "allow_search": allow_search
#         }

#         response = requests.post(API_URL, json=payload)
#         if response.status_code == 200:
#             response_data = response.json()
#             if "error" in response_data:
#                 st.error(response_data["error"])
#             else:
#                 st.subheader("Response:")
#                 st.markdown(f"**Output:** {response_data}")
#         else:
#             st.error("Failed to get response from backend.")



# backend.py

import streamlit as st
import requests
import os

st.set_page_config(page_title="Your Personal helper", layout="centered")
st.title("🧠 AI Chatbot • Transcriber • Moderator")

# 🚀 Step 1: Task Type Selection
task_type = st.selectbox("Choose Task Type:", ["chat", "transcription", "moderation"])

# ✍️ Common Inputs
system_prompt = st.text_area("System Prompt:", height=150, placeholder="E.g. You are a helpful assistant.")
provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama3-70b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# 🔘 Model Selector
selected_model = st.selectbox(
    "Select Model:",
    MODEL_NAMES_GROQ if provider == "Groq" else MODEL_NAMES_OPENAI
)

# 🔍 Web search toggle (only for chat)
allow_search = st.checkbox("Enable Web Search") if task_type == "chat" else False

# 💬 Inputs based on task type
user_input = ""
uploaded_file = None

if task_type in ["chat", "moderation"]:
    user_input = st.text_area("Enter your input:", height=150, placeholder="Type your query or text to moderate")
elif task_type == "transcription":
    uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav", "m4a"])
    if uploaded_file:
        user_input = uploaded_file.name

# 🟢 Backend URL
API_URL = "http://127.0.0.1:9999/chat"

# 🚀 Run Task
if st.button("Run Task"):
    if (user_input.strip() or task_type == "transcription") and (task_type != "transcription" or uploaded_file):
        # Save file if transcription
        if task_type == "transcription" and uploaded_file:
            save_path = f"./temp_uploads/{uploaded_file.name}"
            os.makedirs("temp_uploads", exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.read())
            user_input = save_path  # Replace input with file path

        # Prepare payload
        payload = {
            "task_type": task_type,
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_input],
            "allow_search": allow_search
        }

        # Send request
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Response:")
                if task_type == "chat":
                    st.markdown(f"**Output:** {response_data}")
                elif task_type == "moderation":
                    st.markdown(f"**Moderation Result:** {response_data.get('moderation_result', 'N/A')}")
                elif task_type == "transcription":
                    st.markdown(f"**Transcription Result:** {response_data.get('transcription_result', 'N/A')}")
        else:
            st.error("Failed to get response from backend.")
    else:
        st.warning("Please provide required input or upload a file.")
