#frontend ----> API ----> logic ----> database ----> Response
#api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys,os

# Import TaskManager from src

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from SRC.logic import TaskManager

#-----------------------App Setup-----------------------

app=FastAPI(title="Poll Management API", version="1.0.0")

#------------------------Allow frontend(Streamlit/React) to call the API------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
# Create a poll manager
task_manager = TaskManager()

#-----------Data Models----------------
class Task(BaseModel):
    """
    Data model for a poll.
    """
    id: str
    option: str
    votes: int
    
class UpdateVotes(BaseModel):
    """
    Data model for updating votes.
    """
    votes: int

#----------------API End Points----------

@app.get("/")
def home():
    """
    Check if the API is running.
    """
    return {"message": "Poll Management API is running."}

@app.get("/tasks")
def get_tasks():
    """
    Fetch all polls.
    """
    task_manager = TaskManager()
    result = task_manager.fetch_polls()
    
    if result.get("error"):
        raise HTTPException(status_code=500, detail=result["error"])
    
    return task_manager.get_tasks()

@app.post("/tasks")
def create_task(task: BaseModel):
    """
    Create a new poll.
    """
    task_manager = TaskManager()
    result = task_manager.add_poll(task.id, task.option, task.votes)
    
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["error"])
    
    return {"message": result["message"]}
@app.put("/tasks/{task_id}")
def update_task(task_id: str, votes: int):
    """
    Update a poll's votes.
    """
    task_manager = TaskManager()
    result = task_manager.modify_poll(task_id, votes)
    
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["error"])
    
    return {"message": result["message"]}
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    """
    Delete a poll.
    """
    task_manager = TaskManager()
    result = task_manager.remove_poll(task_id)
    
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["error"])
    
    return {"message": result["message"]}

#-----RUN----

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)
    