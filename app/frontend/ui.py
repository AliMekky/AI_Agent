import streamlit as st
import requests
from app.config.settings import settings
import app.common.logger as logger
import app.common.custom_exception as CustomException

logger = logger.get_logger(__name__)

st.set_page_config(page_title="Multi-AI Agent", layout="centered")
st.title("Multi-AI Agent Interface")

system_prompt = st.text_area("Define your AI Agents: ", height = 70)

selected_model = st.selectbox("Select Language Model:", settings.ALLOWED_MODEL_NAMES)

allow_web_search = st.checkbox("Enable Web Search", value=False)

user_query = st.text_area("Enter your query:", height=150)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent") and user_query.strip():
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }
    ## payload is the information that will be sent into the backend
    ## and then the backend will use them to ask the LLM


    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            ai_response = response.json().get("response", "No response from AI agent.")
            st.subheader("AI Agent Response:")
            st.markdown(ai_response.replace("\n", "<br>"), unsafe_allow_html=True)
            logger.info("AI response successfully retrieved and displayed.")
        else:
            logger.error(f"API returned error status: {response.status_code}")
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        error_message = str(CustomException.CustomException("API request failed", e))
        st.error(f"Error: {error_message}")
        logger.error(f"API request failed: {error_message}")