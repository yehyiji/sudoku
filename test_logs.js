
    const puppeteer = require("puppeteer-core");
    (async () => {
      const browser = await puppeteer.launch({
          executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
          headless: "new"
      });
      const page = await browser.newPage();
      
      const errors = [];
      const logs = [];
      page.on("console", msg => logs.push(msg.text()));
      page.on("pageerror", err => errors.push(err.toString()));
      
      await page.goto("file:///Users/eijiyeh/Documents/sudoku/index.html", {waitUntil: "networkidle0", timeout: 15000});
      await new Promise(r => setTimeout(r, 2000));
      
      console.log("=== ERRORS ===");
      errors.forEach(e => console.log(e));
      console.log("=== LOGS ===");
      logs.filter(l => l.toLowerCase().includes("error") || l.includes("Failure") || l.includes("Exception"))
          .forEach(l => console.log(l));
      
      await browser.close();
    })();
    