from fastapi import Body, Request, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from instructions import Instructions
from pyppeteer import launch
from vizdiff import visual_inspection

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

async def run_lookout(instructions: Instructions, photo_name: str):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(instructions.website)

    for command in instructions.commands:
        await command.execute(browser)
    
    save_path = f"photos/{instructions.project_id}/{photo_name}"
    await page.screenshot({'path': save_path})
    visual_inspection(instructions.project_id)


@app.post("/seedProject")
async def seedProject(instructions: Instructions):
    await run_lookout(instructions, "previous.png")


@app.post("/inspect")
async def inspectProject(instructions: Instructions):
    await run_lookout(instructions, "current.png")


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
