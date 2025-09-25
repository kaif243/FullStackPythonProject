# src logic.py

from SRC.db import DatabaseManager

class TaskManager:
    """
    Acts as a bridge between frontend (streamlit/FastAPI) and the database.
    """
    def __init__(self):
        # create a database managaes instance (this will handes actual db operation )
        
        self.db_manager = DatabaseManager()
        
        
    #------Create------
    def add_poll(self, id, option, votes):
        """
        Add a new poll to the database.
        Return the result of the database operation.
        """
        if not id or not option or votes is None:
            return {"error": "ID, option, and votes are required."}
        
        # Call the database manager to create a new poll
        result=self.db_create_poll(id, option, votes)
    
        if result.get("error"):
            return {"error": "Failed to create poll."}
        
        else:
            return {"message": "Poll created successfully."}
        
    #----Read-----
    def fetch_polls(self):
        """
        Fetch all polls from the database.
        Return the list of polls or an error message.
        """
        return self.db_manager.get_poll()
    
    #-----Update-----
    def modify_poll(self, id, votes):
        """
        Update the votes of a poll.
        Return the result of the database operation.
        """
        if not id or votes is None:
            result = self.db_manager.update_poll(id, votes)
        
        if result.get("error"):
            return {"error": "Failed to update poll."}
        
        else:
            return {"message": "Poll updated successfully."}
    
    def remove_poll(self, id):
        """
        Delete a poll from the database.
        Return the result of the database operation.
        """
        if not id:
            return {"error": "ID is required."}
        
        result = self.db_manager.delete_poll(id)
        
        if result.get("error"):
            return {"error": "Failed to delete poll."}
        
        else:
            return {"message": "Poll deleted successfully."}
        

        
       