import speech_recognition as sr

print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()

mic_index = 1  # Change this to the correct index for your mic
with sr.Microphone(device_index=mic_index) as source:
    print("Say something:")
    audio = r.listen(source, timeout=5, phrase_time_limit=4)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except Exception as e:
    print(f"Error: {e}")
