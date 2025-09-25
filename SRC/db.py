import os
from supabase import create_client, Client
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url, key)

def create_poll(id,option,votes):
    return supabase.table("poll").insert({
        "id":id,
        "option":option,
        "votes":votes
        }).execute()
#get All task
def get_poll():
    return supabase.table("poll").select("*").execute()

#get task status
def update_poll(id,votes):
    return supabase.table("poll").update({
        "votes":votes
        }).eq("id",id).execute()
    
#delete task    
def delete_poll(id):
    return supabase.table("poll").delete().eq("id",id).execute()


 