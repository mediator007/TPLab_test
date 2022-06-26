from dataclasses import dataclass, field
import datetime

@dataclass
class ScreenshotStatistic:
    url: str
    user_id: int
    created: datetime = field(default_factory=datetime.now)