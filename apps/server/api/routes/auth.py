from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from auth.jwt import get_current_user, TokenData, create_access_token
from database.session import get_db
from models.user import User
from sqlmodel import Session, select
import bcrypt

# Create the API router
router = APIRouter()

class UserResponse(BaseModel):
    id: str
    email: str
    name: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    token: str
    user: UserResponse

@router.post("/login", response_model=AuthResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate user and return JWT token.
    """
    # Find user by email
    statement = select(User).where(User.email == request.email)
    user = db.exec(statement).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Verify password
    if not bcrypt.checkpw(request.password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Create JWT token
    token = create_access_token(data={"sub": user.id, "email": user.email})
    
    return AuthResponse(
        token=token,
        user=UserResponse(id=user.id, email=user.email, name=user.name)
    )

@router.post("/register", response_model=AuthResponse)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new user and return JWT token.
    """
    # Check if user already exists
    statement = select(User).where(User.email == request.email)
    existing_user = db.exec(statement).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password
    hashed_password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create user
    user = User(email=request.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    # Create JWT token
    token = create_access_token(data={"sub": user.id, "email": user.email})
    
    return AuthResponse(
        token=token,
        user=UserResponse(id=user.id, email=user.email, name=user.name)
    )

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: TokenData = Depends(get_current_user)
):
    """
    Get information about the currently authenticated user.
    """
    return UserResponse(
        id=current_user.user_id,
        email=current_user.email,
        name=current_user.name if hasattr(current_user, 'name') else None
    )