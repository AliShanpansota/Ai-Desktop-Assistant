import speech_recognition as sr

print("Available microphones:")
for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {mic_name}")

mic_index = int(input("Enter the mic index to use: "))

r = sr.Recognizer()
with sr.Microphone(device_index=mic_index) as source:
    print("Adjusting for ambient noise...")
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something:")
    try:
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.WaitTimeoutError:
        print("Timeout: Didn't hear anything.")
    except Exception as e:
        print(f"Error: {e}")
