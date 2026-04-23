from config import TARGET_USER

def parse_chat(chat_text):
    """Split chat into lines"""
    return chat_text.strip().split("\n")

def is_last_message_from_target(chat_text):
    """Check if last message is from target user"""
    lines = parse_chat(chat_text)

    if not lines:
        return False

    last_line = lines[-1]

    print(f"[DEBUG] Last message: {last_line}")

    return TARGET_USER.lower() in last_line.lower()