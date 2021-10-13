import asyncio
import uuid

from fastapi import Body, Request, FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from commands import Command
from pyppeteer import launch


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3232",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/seedProject")
async def seedProject():
    pass


async def testPyppeteer():
    test_page = "https://google.com"
    browser = await launch()
    page = await browser.newPage()
    await page.goto(test_page)
    await page.screenshot({'path': f'photos/example.png'})
    await browser.close()

@app.post("/test")
async def testLookout():
    await testPyppeteer()
