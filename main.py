from fastapi import FastAPI, HTTPException, status, UploadFile, Form, Query
from core import config
from core.model import ResUserModel, ReqUserModel, BaseUserModel, LoginModel, RegisterModel, FileModel, Editmodel
from core.schema import UserTable, PapersTable
import time
from core.utility import getPassHash
dbr = config.getDb()
app = FastAPI()
@app.get("/")
async def get_users():
    return {"message": dbr}
@app.get("/user/{id}", response_model=ResUserModel)
def get_user_by_id(id: int):
    user = dbr.query(UserTable).filter(UserTable.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No user found with id {id}")
    return user

@app.post("/user/register", response_model=RegisterModel, status_code=status.HTTP_201_CREATED)
def create_user(user_model: ReqUserModel):
    tkn = getPassHash(user_model.email + user_model.password)
    user = dbr.query(UserTable).filter(UserTable.email == user_model.email).first()
    if user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User with email {user_model.email} already exists!")
    new_user = UserTable(name=user_model.name, email=user_model.email, password=user_model.password, token=tkn)
    dbr.add(new_user)
    dbr.commit()
    dbr.refresh(new_user)
    return new_user

@app.post("/user/login")
async def login(user_detail: LoginModel):
    new_token = getPassHash(user_detail.email + user_detail.password)
    result = dbr.query(UserTable).filter(UserTable.token == new_token).first()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect email or password")
    return {"msg": "Login successful"}

@app.get("/users", response_model=list[ResUserModel])
def get_all_users() -> any:
    user_list = dbr.query(UserTable).all()
    return user_list

@app.put("/user/{id}", response_model=ResUserModel)
def update_user(id: int, update_model: BaseUserModel):
    user = dbr.query(UserTable).filter(UserTable.id == id)
    if user.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} doesn't exist!")
    
    if update_model.name is not None:
        if update_model.email is not None:
            user.update(update_model.model_dump())
        else:
            user.update({'name': f'{update_model.name}'})
    else:
        if update_model.email is not None:
            user.update({'email': f'{update_model.email}'})
    dbr.commit()
    return user.first()

@app.delete("/user/delete/{id}")
def delete_user(id: int):
    user = dbr.query(UserTable).filter(UserTable.id == id)
    if user.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} doesn't exist!")
    user.delete()
    dbr.commit()
    return {"msg": "User deleted successfully!"}

@app.post("/paper/upload")
async def upload_file(file:UploadFile, year: str = Form(..., min_length=4, max_length=4), sem: int = Form(...), 
    dept: str = Form(...), sub: str = Form(...)):
    filename = str(time.time()).split(".").pop()
    file_ext = file.filename.split(".").pop()
    file_path = f"files/{filename}.{file_ext}"
    content = file.file.read()
    with open(file_path, "wb") as fp:
        fp.write(content)
    new_file = PapersTable(file=file_path, year=year, sem=sem, dept=dept, sub=sub)
    dbr.add(new_file)
    dbr.commit()
    dbr.refresh(new_file)
    return {
        "msg": "File uploaded successfully!",
        "details": new_file
    }

@app.get("/paper/find")
async def get_all_papers():
    all_records = dbr.query(PapersTable).all()
    return {"total": f"Total {len(all_records)} papers found of all dept!", "details of the paper are:": all_records}

@app.get("/paper/dept/find")
async def papers_of_dept(dept: str):
    records = dbr.query(PapersTable).filter(PapersTable.dept == dept).all()
    if records is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No records found!")
    return records

@app.post("/paper/delete/{id}")
async def deletePaper(id: int):
    paper = dbr.query(PapersTable).filter(PapersTable.id == id)
    if paper.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Paper with id {id} doesn't exist!")
    paper.delete()
    dbr.commit()
    return {"msg": "Paper deleted successfully!"}
@app.delete("/paper/delete/{id}")
def deletePaper(id: int):
    paper = dbr.query(PapersTable).filter(PapersTable.id == id)
    if paper.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Paper with id {id} doesn't exist!")
    paper.delete()
    dbr.commit()
    return {"msg": "Paper deleted successfully!"}
#edit paper details
@app.put("/paper/edit/{id}")
def editPaper(id: int, newmodel: Editmodel):
    paper = dbr.query(PapersTable).filter(PapersTable.id == id)
    if paper.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Paper with id {id} doesn't exist!")
    paper.update({'year': f'{newmodel.year}', 'sem': f'{newmodel.sem}', 'dept': f'{newmodel.dept}', 'sub': f'{newmodel.sub}'})
    dbr.commit()
    return {"msg": "Paper details updated successfully!"}