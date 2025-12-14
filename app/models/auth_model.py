
from dataclasses import dataclass
from typing import Optional


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
