
from dataclasses import dataclass
from typing import Optional


@dataclass
class Preferences:
    dateFormat: Optional[str] = None
    hourFormat: Optional[str] = None
    language: Optional[str] = None
    theme: Optional[str] = None
    timeZone: Optional[str] = None
    notifications: Optional[dict] = None  # Could be another nested dataclass if needed

@dataclass
class AuthenticationModel:
    accessToken: Optional[str] = None
    refresh_token: Optional[str] = None

    userId: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None

    firstName: Optional[str] = None
    lastName: Optional[str] = None

    isActive: Optional[bool] = None
    isBlocked: Optional[bool] = None
    isConfirmedUser: Optional[bool] = None
    mustChangePassword: Optional[bool] = None

    loginAttempts: Optional[int] = None

    photo: Optional[str] = None
    recoveryToken: Optional[str] = None

    blockedDate: Optional[str] = None
    lastLoginDate: Optional[str] = None
    lastPasswordChangeDate: Optional[str] = None
    tokenExpirationDate: Optional[str] = None
    sessionId: Optional[int] = None
    
    rol: Optional[str] = None
    preferences: Optional[Preferences] = None

    def __post_init__(self):
        if self.preferences and isinstance(self.preferences, dict):
            self.preferences = Preferences(**self.preferences)
