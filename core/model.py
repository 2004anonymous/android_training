from pydantic import BaseModel, EmailStr
from fastapi import UploadFile, File

class BaseUserModel(BaseModel):
    name : str = None
    email : EmailStr = None

class ReqUserModel(BaseUserModel):
    password : str

class ResUserModel(BaseUserModel):
    id: int

class LoginModel(BaseModel):
    email:EmailStr
    password:str

class RegisterModel(BaseModel):
    token : str

class FileModel(BaseModel):
    file : UploadFile = File()
    year : str
    sem : int
    dept : str
    sub : str
class Editmodel(BaseModel):
    id: int
    year: str
    sem: int
    dept: str
    sub: str


