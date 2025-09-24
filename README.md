#  Smart Polling App

The Smart Polling App is a console-based Python application that allows users to cast votes digitally for different poll options. It provides an easy way to collect and display votes without a web interface.

## Features

- **User-Friendly Interface**:Easy console-based menu for voting and results.

- **Poll Options Display**:Shows all available options dynamically.

- **Vote Casting**:Users can select and submit their votes.

- **Vote Storage**:Saves votes in CSV or SQLite for persistence.

- **Results Display**:Shows vote counts and percentages clearly.

- **Data Integrity**:Ensures votes are accurately recorded.

- **Future Enhancements**:Prevent multiple votes, add charts, or multiple polls.

## Project Structure

smart_polling_app/
│
|---SRC/                        #core application logic
|    |---logic.py               #Business logic and task
operations
|    |__db.py                   #Database operations
|
|----API/                       #Backend API
|    |__main.py                 #FastAPI endpoints
|
|----FRONT END/                 #frontend application
|    |__app.py                  #Streamlit web interface
|
|____requirements.txt           #python dependence
|_____.env                       #Python variables
|____README.md                  #Project documentation



## Quick Start

### Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push,Cloning)

### 1. Clone or Download the Project
# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract zip files

### 2. Install Dependicies
pip install -r requirements.txt

### 3. Set up Supabase Database
1. Create a Supabse Project:

2. Create a Task  table:

- Go to the SQL Editor in your Supabase
dashboard
- Run this SQL command:

```sql

## 4.Configure Envinorment Variables

1.