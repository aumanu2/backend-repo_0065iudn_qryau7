"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Add your own schemas here:
# --------------------------------------------------

class BtechApplication(BaseModel):
    """
    B.Tech Program application schema
    Collection name: "btechapplication"
    """
    full_name: str = Field(..., description="Applicant's full name")
    email: EmailStr = Field(..., description="Applicant email")
    phone: str = Field(..., min_length=7, max_length=20, description="Contact number")
    parent_name: Optional[str] = Field(None, description="Parent/Guardian name")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State")
    grade_level: Literal['11', '12', 'Gap Year', 'Other'] = Field(..., description="Current grade level")
    stream: Optional[Literal['PCM', 'PCMB', 'Science', 'Commerce', 'Arts', 'Other']] = Field(None, description="Academic stream")
    program_interest: Optional[str] = Field(None, description="Interested specialization or branch")
    preferred_intake: Optional[str] = Field(None, description="Preferred intake/session")
    how_heard: Optional[str] = Field(None, description="How did you hear about us")
    consent: bool = Field(..., description="Consent to be contacted and to privacy policy")
