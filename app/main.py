from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     # Initialize any required resources here
#     pass

@asynccontextmanager
async def lifespan(app:FastAPI):
    pass

@app.post("/webhook/vapi")
async def handle_vapi_webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    background_tasks.add_task(process_webhook, data)
    return JSONResponse({"status": "received"})

async def process_webhook(data):
    # This function will be called in the background for async processing
    # It should route the call to the appropriate handler (see Call Router)
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
