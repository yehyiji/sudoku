import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True, executablePath='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    page = await browser.newPage()
    await page.goto('http://localhost:3000/?v=3', {'waitUntil': 'networkidle0'})
    
    body_text = await page.evaluate('document.body.innerText')
    print("BODY TEXT:\n", body_text)
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
