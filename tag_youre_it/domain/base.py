from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseDomain:
    created_at: datetime
    updated_at: datetime
