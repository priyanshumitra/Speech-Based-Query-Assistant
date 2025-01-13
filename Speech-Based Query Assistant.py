import wolframalpha
import webbrowser
from tkinter import *
import speech_recognition as sr

def create_window(answer):
    """Creates a Tkinter window to display the answer."""
    window = Tk()
    window.geometry("700x600")
    label = Label(
        window,
        justify=LEFT,
        wraplength=650,
        compound=CENTER,
        padx=10,
        text=answer,
        font="times 15 bold"
    )
    label.pack()
    # Close window after 10 seconds
    window.after(10000, lambda: window.destroy())
    window.mainloop()


def get_wolframalpha_answer(query, client):
    """Fetches the answer from Wolfram|Alpha."""
    try:
        res = client.query(query)
        answer = next(res.results).text
        return answer
    except Exception:
        return None


def search_google(query):
    """Opens the default web browser to search Google."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def main():
    recognizer = sr.Recognizer()
    app_id = "VX33U8-JVT99X5EK8"  # Replace with your Wolfram|Alpha app ID
    client = wolframalpha.Client(app_id)

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source)
                print("Recognizing...")
                query = recognizer.recognize_google(audio)
                print(f"You said: {query}")
                
                if query.lower() == "stop":
                    print("Exiting program...")
                    break
                
                # Fetch answers
                answer = get_wolframalpha_answer(query, client)
                if answer:
                    print("Answer from Wolfram|Alpha:", answer)
                    create_window(answer)
                else:
                    print("No results from Wolfram|Alpha. Opening Google search...")
                    search_google(query)
            
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Speech Recognition error: {e}")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
