# Speech-Based-Query-Assistant
This project enables users to perform natural language queries using speech. It leverages Wolfram|Alpha to fetch direct answers to questions and falls back on Google Search when specific results aren't available. The project is built in Python, using libraries such as speech_recognition, wolframalpha, tkinter, and webbrowser.

Features:

Voice Input Recognition:

Utilizes the speech_recognition library to capture and interpret user queries through voice.
Processes queries in real time.

Wolfram|Alpha Integration:

Uses the Wolfram|Alpha API to fetch precise and computational answers to a wide variety of queries.

Google Search Fallback:

Redirects to Google Search when no results are available from Wolfram|Alpha.

Graphical Answer Display:

Displays the answer from Wolfram|Alpha in a Tkinter window with a clean and readable layout.

Automatically closes the display window after 10 seconds.

Voice Command Control:

Say "stop" to terminate the program gracefully.

Prerequisites:

Python 3.7 or above.

Wolfram|Alpha Developer Account for API Key.

Internet access for both Wolfram|Alpha queries and Google Search.

Libraries Used:

speech_recognition: For capturing and recognizing user speech.

wolframalpha: For accessing the Wolfram|Alpha API.

tkinter: For graphical display of answers.

webbrowser: To open Google search results in a browser.

Setup Instructions:

Clone the repository:

bash
Copy code

git clone https://github.com/your-username/speech-based-query-assistant.git
cd speech-based-query-assistant

Install the required dependencies:

bash
Copy code

pip install speechrecognition wolframalpha

Replace the placeholder Wolfram|Alpha App ID in the code:

Find the line: app_id = "VX33U8-JVT99X5EK8" and replace it with your own Wolfram|Alpha API Key.

Run the program:

bash
Copy code

python main.py

How to Use:

Speak your query clearly when prompted with "Listening...".

Wait for the system to process and display the result.

If Wolfram|Alpha cannot provide an answer, Google Search will open in your default browser.

Say "stop" to exit the application.

Example Use Cases:

"What is the capital of France?"

"Solve x^2 + 2x - 8 = 0."

"What is the weather like in New York?"
