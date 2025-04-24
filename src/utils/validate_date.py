from datetime import datetime
from typing import Optional

from fastapi import HTTPException


def validate_date(date_string: Optional[str]):
    if date_string:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format, use YYYY-MM-DD")
    return None
