from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
import sys

sys.path.append("C:/Project_pharmacy/src")
sys.path.append("C:/Project_pharmacy")

from src.server.groups.routers import router as group_router
from src.server.manager.routers import router as manager_router
from src.server.employees.routers import router as employee_router
from src.server.administrator.routers import router as admin_router
from src.server.medicines.routers import router as medicine_router
from src.server.suppliers.routers import router as supplier_router
from src.server.supplies.routers import router as supplies_router
from src.server.clients.routers import router as clients_router
from src.server.orders.routers import router as orders_router
from src.server.sclad.routers import router as sclad_router
from src.server.ostatki.routers import router as ostatki_router
from src.server.pokypky.routers import router as pokupky_router

app = FastAPI()

app.include_router(group_router)
app.include_router(manager_router)
app.include_router(employee_router)
app.include_router(admin_router)
app.include_router(medicine_router)
app.include_router(supplier_router)
app.include_router(supplies_router)
app.include_router(clients_router)
app.include_router(orders_router)
app.include_router(sclad_router)
app.include_router(ostatki_router)
app.include_router(pokupky_router)

@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == "__main__":

    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
