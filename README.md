# web-calculator

Web Calculator with Frontend and Backend

This project creates a simple online calculator that uses a webpage (frontend) to send numbers and operations to a server (backend). The server performs the calculation and sends back the answer to display on the webpage.
What You Need

    Python installed on your computer
    A code editor (like Notepad or VSCode)
    A web browser (like Chrome)

How to Set It Up and Use
1. Create a Folder

Make a new folder named web-calculator.
2. Prepare Files

Inside this folder, create two files:

    app.py (for the backend Python code)
    index.html (for the webpage)

3. Write the Backend Code

Open app.py in your editor and copy the backend code provided earlier. This code creates a server that listens for calculation requests.
4. Write the Frontend Code

Open index.html in your editor and copy the frontend code provided earlier. This creates a webpage with input fields, a dropdown for operations, and a button.
5. Install Required Python Packages

Open your terminal or command prompt, navigate to your project folder, and install Flask and Flask-CORS with the following command:

    Using Python 3:
    pip install flask flask-cors

6. Run the Backend Server

In the terminal, start your backend server by running:
python app.py

Your server will be active and listening on http://127.0.0.1:5000/.
7. Serve the Webpage

In the same terminal, run a local server to serve your webpage:

    Command:
    python -m http.server 8000

Now, open your browser and go to:
http://localhost:8000/index.html
8. Use the Calculator

    Enter two numbers
    Choose an operation (+, -, *, /)
    Click Calculate
    See the result appear below

Troubleshooting Tips

    Ensure the backend is running before opening the webpage.
    Access your webpage via http://localhost:8000/index.html.
    If you encounter errors, check the terminal and browser console for messages.

Summary

    Run backend with python app.py.
    Serve webpage with python -m http.server 8000.
    Open webpage in your browser.
    Input data and get calculations dynamically.

