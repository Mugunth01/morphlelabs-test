from flask import Flask
import os
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Personal Details
    name = "Your Full Name"  # Replace with your full name
    username = os.getlogin()  # System username
    
    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Top command output
    top_output = subprocess.getoutput('top -b -n 1 | head -15')  # Fetches top 15 lines for brevity
    
    # Create HTML response
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre><strong>Top Output:</strong><br>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
