from dotenv import load_dotenv 
from dataclasses import dataclass
import os
import sys

@dataclass
class Config:
    api_token: str
    base_url: str
    course_ids: list[int]
    poll_interval: int = 300
    notification_method: str = "console"
    discord_webhook_url: str = ""

def load_config():
    load_dotenv()

    api_token = os.getenv("CANVAS_API_TOKEN")
    base_url = os.getenv("CANVAS_BASE_URL")
    raw_course_ids = os.getenv("CANVAS_COURSE_IDS")

    if not api_token or not base_url or not raw_course_ids:
        raise ValueError("Missing required env vars: API_TOKEN or BASE_URL or CANVAS_COURSE_IDS")

    course_ids = [int(course) for course in raw_course_ids.split(",")]

    return Config(
            api_token=api_token,
            base_url=base_url,
            course_ids=course_ids,
            poll_interval=int(os.getenv("POLL_INTERVAL") or 300),
            notification_method=(os.getenv("NOTIFICATION_METHOD") or "console"),
            discord_webhook_url=(os.getenv("DISCORD_WEBHOOK_URL") or ""),
            )
