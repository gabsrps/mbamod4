// Gera PDF A4 a partir do HTML: node pdf.js entrada.html saida.pdf
const path = require('path');
const pwPath = process.env.PLAYWRIGHT_CORE ||
  '/inner_container/opt/toolchains/.nvm/versions/node/v22.23.4/lib/node_modules/@playwright/mcp/node_modules/playwright-core';
const { chromium } = require(pwPath);

(async () => {
  const [input, output] = process.argv.slice(2);
  const browser = await chromium.launch({
    executablePath: process.env.CHROME || '/inner_container/opt/playwright/chromium-1232/chrome-linux64/chrome',
    args: ['--no-sandbox'],
  });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input));
  await page.pdf({ path: output, preferCSSPageSize: true, printBackground: true });
  await browser.close();
})();
