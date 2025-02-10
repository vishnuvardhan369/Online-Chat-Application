# Online Chat Application

Online Chat is a robust, real-time chat application built using Flask for the backend and a responsive HTML/CSS/JavaScript frontend. It enables users to send messages and share files from any device, including mobile, using an ngrok tunnel to expose the server online.

## Overview

This project provides the following features:
- **Real-Time Messaging:** Send and receive messages instantly from any device.
- **File Transfer:** Upload files from your device and download them with a single click.
- **Cross-Device Access:** Access the chat application remotely via an ngrok-generated public URL.
- **User-Friendly Interface:** A clean, responsive UI built with HTML, CSS, and JavaScript that displays messages with timestamps.

## Technologies Used

- **Backend:** Python, Flask, JSON, threading, HTTPServer
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** ngrok for external tunneling

## Project Structure

Online-Chat-Application/  
&nbsp;&nbsp;&nbsp;&nbsp;├── server.py  — Flask backend handling chat messages, file uploads/downloads, and API endpoints    
&nbsp;&nbsp;&nbsp;&nbsp;├── index.html — Frontend web interface for sending messages and files    
&nbsp;&nbsp;&nbsp;&nbsp;└── README.md  — This documentation file


**Installation:**  
1. Clone the repository:  
   `git clone https://github.com/vishnuvardhan369/Online-Chat-Application`  
2. Navigate to the project directory:  
   `cd Online-Chat-Application`  
3. Install the required dependencies using pip:  
   `pip install Flask`


**Usage:**  
- **Start the Server:** 
In your terminal, navigate to the project directory and run:n:  
  `python server.py`  

This starts the Flask server on 0.0.0.0 at port 8000 by default, handling chat messages and file transfers.
- **Run the Client:** Open another terminal (or use an IDE), navigate to the project directory, and run:  
  `python client.py`

- **Expose the Server Online:** 
Use ngrok to tunnel the server for external access:
  `ngrok http 8000`
Ngrok will provide a public URL (e.g., https://6322-103-5-112-80.ngrok-free.app) that you can share with others to access the chat from any device.

- **Access the Chat Application:** Open a web browser and navigate to the ngrok URL. The chat interface (from index.html) will load and prompt you to enter your username.
- **Using the Application:** Messaging: Type your message in the input field and press Enter or click the Send button to broadcast it.
File Transfer: Click the Upload button, select a file, and the file will be sent to the chat. Files appear as clickable links that users can download.
The client polls the server for new messages every 2 seconds, ensuring real-time updates.




