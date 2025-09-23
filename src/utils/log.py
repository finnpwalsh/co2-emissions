from datetime import datetime

def info(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
