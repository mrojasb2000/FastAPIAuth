from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer("/token")


@app.get("/")
def index():
    return "Welcome to FastAPI"


@app.get("/users")
def users(token: str = Depends(oauth2_scheme)):
    return "User list"


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return form_data.username
