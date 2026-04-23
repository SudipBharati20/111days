import time
from automation import open_chat_app, wait_for_app
from chat_reader import copy_chat_history
from analyzer import is_last_message_from_target
from gpt_response import generate_roast
from responder import send_response
from config import SHORT_DELAY, LONG_DELAY

def main():
    print("🔥 Naruto Chat Bot Started...")

    open_chat_app()
    wait_for_app()

    while True:
        try:
            chat = copy_chat_history()

            if not chat:
                continue

            if is_last_message_from_target(chat):
                print("[INFO] Target message detected!")

                reply = generate_roast(chat)
                print(f"[BOT] {reply}")

                send_response(reply)

                time.sleep(LONG_DELAY)

            time.sleep(SHORT_DELAY)

        except KeyboardInterrupt:
            print("\n[INFO] Stopped by user")
            break

        except Exception as e:
            print("[ERROR]", e)
            time.sleep(2)

if __name__ == "__main__":
    main()