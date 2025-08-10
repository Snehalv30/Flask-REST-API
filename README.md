# Flask-REST-API

This project is a simple REST API built with Python Flask that demonstrates basic CRUD (Create, Read, Update, Delete) operations for managing user data.
It is developed as part of Internship Task 4.

# Features
GET → Fetch all users or a single user by ID

POST → Add a new user

PUT → Update user details

DELETE → Remove a user

JSON-based API responses

Flask development server with debug mode enabled

# Tech Stack
Python 3.10+
Flask
Flask-RESTful 
JSON

# Installation & Setup
1️⃣ Clone the Repository
'''bash
Copy
Edit
git clone (https://github.com/Snehalv30/Flask-REST-API).git

2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4️⃣ Run the Application
bash
Copy
Edit
python app.py
The server will start at:

cpp
Copy
Edit
http://127.0.0.1:5000
📬 API Endpoints 
Method	   Endpoint	        Description
GET	       /users	          Get all users
GET	       /users/<id>	    Get user by ID
POST	     /users	          Create a new user
PUT	       /users/<id>	    Update user details
DELETE	   /users/<id>	    Delete a user
