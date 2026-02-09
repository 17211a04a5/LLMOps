import streamlit as st
import requests

from app.common.logger import get_logger
from app.common.customException import CustomException
from app.config.settings import settings

logger = get_logger(__name__)



st.set_page_config(page_title="MultiAgent UI", page_icon="🤖",layout="centered")
st.title("MultiAgent UI - Powered by FastAPI and Streamlit")

system_prompt = st.text_area("System Prompt", "You are a helpful assistant.")
allow_models = st.selectbox("Allow models",settings.ALLOWED_MODELS, index=1)
allow_search = st.checkbox("Allow Search?", value=True)

user_query = st.text_area("Enter your query:",height=100)


API_URL = "http://localhost:8000/get-response"

if st.button("ask Agent") and user_query.strip():
    try:
        payload = {
            "model_name": allow_models,
            "system_prompt": system_prompt,
            "messages":[ user_query ],
            "allow_search": allow_search,
        }
        logger.info(f"Sending request to API with payload: {payload}")
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            agent_response = response.json().get("response", "No response received.")
            st.subheader("Response from MultiAgent:")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)
        else:
            logger.error(f"API returned error: {response.status_code} - {response.text}")
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        logger.error(f"Error during API call", exc_info=True)
        st.error("An error occurred while communicating with the MultiAgent API.")
        raise CustomException("An error occurred while communicating with the MultiAgent API.", error_detail=e)
        

