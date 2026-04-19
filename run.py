import asyncio
from pyppeteer import launch
async def main():
    browser = await launch(headless=True, executablePath='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    page = await browser.newPage()
    await page.goto('http://localhost:3000/test_frame.html', {'waitUntil': 'networkidle2'})
    await page.waitForFunction('document.getElementById("output").innerText !== ""', timeout=5000)
    text = await page.evaluate('document.getElementById("output").innerText')
    print("----- RESULT -----")
    print(text)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
