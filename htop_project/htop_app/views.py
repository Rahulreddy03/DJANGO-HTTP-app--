from django.shortcuts import render

# Create your views here.
import os
import datetime
import subprocess
from django.http import HttpResponse
import getpass

def htop_view(request):
    # Get the current server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the system username using getpass
    username = getpass.getuser()
    
    # Get the top command output (simulating htop)
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8').splitlines()
    except Exception as e:
        top_output = str(e).splitlines()
    
    # Create a simple HTML response
    response = f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> SINGAM RAHUL KUMAR REDDY</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <h2>Top Output:</h2>
            <pre>{'\n'.join(top_output)}</pre>
        </body>
    </html>
    """
    
    return HttpResponse(response)