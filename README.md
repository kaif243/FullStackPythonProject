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
CREATE TABLE poll (
    id INTEGER PRIMARY KEY,
    option TEXT NOT NULL,
    votes INTEGER DEFAULT 0
);

```

 3. Get Your Credentials:

### 4.Configure Envinorment Variables

1.Create a '.env' file in the project root

2. Add your Supabase credentials to `.env` :
   SUPABASE_URL=your_project_url_here
   SUPABASE_KEY=your_anon_key_here


**Example:**

supabase_URL="https://inhnqfddsabdghbbdsje.supabase.co"
supabase_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImluaG5xZmRkc2FiZGdoYmJkc2plIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI1MTgsImV4cCI6MjA3MzY1ODUxOH0.u2N85luRXT2MhR4EfusC3PcXnbv3U75qB_RhNy9rc_U"

### 5. Run The Application

## streamlit Frontend

-streamlit run fronted/app.py

-The app will open in your browser at 'htts://localhost:5000'

## FastAPI backend

cd API
python Main.py

The API will be available at 'http://localhost:5000'

## How to Use Application
##As a Voter:

-You will be taken to the main menu after launching the application.

-From there, you can view all available poll options.

-To cast your vote, select the number corresponding to your preferred option.


##Viewing Results:

-You can choose the “Show Results” option from the main menu.

-The application will display the current vote count and percentage for each poll option.

-This helps users see the popularity of each option in real-time.

## Technical Details

### Technologies Used

- **Frontend**:Streamlit (Python web framework)
- **Backend**:FastAPI (Python REST API framework)
- **Database**: Supabase (PostgreSQL-based-backend-as-a-service)
- **Language**: Python 3.8+

### Key Components 

1. **'SRC/db.py'**: Database operations 

-Handles all CRUD operations with supabase

2. **'SRC/logic.py'**: business logic 

-Task validation and processing 

## Troubleshooting

## Common Issues

1. **"Module not found" errors**

- Make sure you've installed all dependencies:` pip install -r requirements.txt`

- Check that you're running commands from are correct directory

2. **"Votes not updating" errors**

-Ensure that poll.db (SQLite) or poll.csv exists in the project folder.

-Make sure the file has write permissions.

## Future Enhancement:

- **User Authentication**: Implement user accounts and secure login so that each voter can vote only once.

- **Multiple Polls**: Allow creation of multiple polls or questions instead of a single poll, enabling more diverse surveys.

- **Admin Panel**: Add an admin interface to manage polls, options, and view detailed results.

- **Graphical Results**: Integrate charts using libraries like Matplotlib to display results visually.

- **Real-Time Updates**: Enable live result updates as votes are cast, so users can see changing results instantly.

- **Notifications**: Send alerts to users when new polls are available or results are updated.

## support

- If you encounter any issues or have questions:

- **Mobile No**: 7207662495
- **Maild Id**: kaif24sm@gmail.com

