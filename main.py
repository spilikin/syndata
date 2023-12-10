from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from invoices import generate_random_invoice, find_in_bundle
import json

templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/invoices/random")
async def random_invoice():
    invoice = generate_random_invoice()
    return invoice.dict()
  

@app.get("/invoices/random/html", response_class=HTMLResponse)
async def random_invoice_html(request: Request):
    bundle = generate_random_invoice()
    bundle_json = bundle.json(indent=2)
    lines = filter(lambda r: r.resource.resource_type == "ChargeItem", bundle.entry)
    return templates.TemplateResponse(
        "invoice.html",
        {
            "request": request,
            "bundle": bundle,
            "invoice": find_in_bundle(bundle, "Invoice").resource,
            "issuer": find_in_bundle(bundle, "Organization").resource,
            "issuer_location": find_in_bundle(bundle, "Location").resource,
            "bundle_json": bundle_json,
            "lines": lines,
        }
    )


