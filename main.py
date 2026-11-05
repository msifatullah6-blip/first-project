from fastapi import FastAPI
import models
from db import engine
from routers import pasien, poli, dokter, kunjung, auth, periksa, obat, resep

app = FastAPI()

models.base.metadata.create_all(bind=engine)
app.include_router(pasien.router)
app.include_router(poli.router)
app.include_router(dokter.router)
app.include_router(kunjung.router)
app.include_router(auth.router)
app.include_router(periksa.router)
app.include_router(obat.router)
app.include_router(resep.router)

@app.get('/')
def root():
    return{'Message': 'Hello World!'}

@app.get('/greeting/{name}')
def sayHelo(name: str):
    return{'Message': f'Hello {name}!'}