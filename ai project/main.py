from voice_engine import speak, listen

speak("Assistant ready")

while True:
    command = listen()
    if command:
        print(command)