from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agents
from app.common.customException import CustomException
from app.common.logger import get_logger
from app.config.settings import settings

logger = get_logger(__name__)
app = FastAPI(title="Multi-Agent API")

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool



@app.post("/get-response")
def chat_endpoint(request_state: RequestState):
    logger.info(f"Received request for model: {request_state.model_name} with query: {request_state.messages}")
    try:
        if request_state.model_name not in settings.ALLOWED_MODELS:
            raise HTTPException(status_code=400, detail=f"Model '{request_state.model_name}' is not allowed.")
        
        response = get_response_from_ai_agents(
            llm_id=request_state.model_name,
            messages=request_state.messages,
            allow_search=request_state.allow_search,
            system_prompt=request_state.system_prompt
        )

        logger.info(f"Response generated successfully for model: {request_state.model_name}") 
        return {"response": response}
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise CustomException("An error occurred while processing the request.", error_detail=e)

