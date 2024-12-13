from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from mangum import Mangum
from config import Config
from bot_handlers import handle_message, handle_update
import logging


# Import your custom modules if they are compatible with AWS Lambda
# Ensure that 'config' and 'bot_handlers' are included in your deployment package
# from config import Config
# from bot_handlers import handle_message

app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.get("/")
# Added docstring to describe the endpoint
async def index():
    """Endpoint to check if the bot is running."""
    return PlainTextResponse("Welcome to the Audio Transcribe Bot!")

@app.post("/webhook")
# Added docstring to describe the endpoint
async def webhook(request: Request):
    """Endpoint to receive updates from Telegram."""
    try:
        update = await request.json()
        logger.info(f"Received update: {update}")  # Log the received update
        handle_update(update)  # Process the update
        return JSONResponse({'status': 'ok'})
    except Exception as e:
        # Changed from logger.error to logger.exception for better error logging
        logger.exception("Error processing webhook")  # Log the exception
        return JSONResponse({'status': 'error', 'message': str(e)}, status_code=500)

@app.get("/webhook")
# Added docstring to describe the endpoint
async def webhook_get():
    """Endpoint to verify webhook setup."""
    return PlainTextResponse(
        "Webhook is working. Send a POST request with a Telegram update to use the bot.",
        status_code=200
    )
# AWS Lambda handler using Mangum
# handler = Mangum(app) # if using AWS Lambda

