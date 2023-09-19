from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from dbmodels import SessionLocal, engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()
templates = Jinja2Templates(directory='C:/Users/Enots/PycharmProjects/fapilastdz/templates')


app.dependency_overrides[SessionLocal] = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)
