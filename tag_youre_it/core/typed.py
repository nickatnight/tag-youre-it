from typing import Dict, Optional, TypedDict


class RedditClientConfigTyped(TypedDict):
    client_id: str
    client_secret: str
    username: str
    password: str
    user_agent: str
    requestor_kwargs: Optional[Dict]  # type: ignore
