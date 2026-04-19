import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True, executablePath='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', args=['--window-size=1200,800'])
    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 800})
    
    await page.goto('http://localhost:3000/?v=5', {'waitUntil': 'networkidle2'})
    await asyncio.sleep(2)  # Give time for React to render
    
    await page.screenshot({'path': 'final_render_check.png', 'fullPage': True})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
