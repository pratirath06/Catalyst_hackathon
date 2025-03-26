# speech_recognition.py file 
import speech_recognition as sr
import logging

def process_voice_input(audio_data):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_data) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            return text
    except sr.UnknownValueError:
        logging.error("Speech Recognition could not understand audio")
        return "Sorry, I couldn't understand that. Could you please try again or type your question?"
    except sr.RequestError as e:
        logging.error(f"Could not request results from speech recognition service; {e}")
        return "Sorry, there was an error processing your voice input. Please try again or type your question."
    except Exception as e:
        logging.error(f"Error in voice transcription: {e}")
        return "Sorry, I couldn't process that audio. Could you please type your question?"