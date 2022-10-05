from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class BaseDomain:
    ref_key: UUID
    created_at: datetime
    updated_at: datetime
