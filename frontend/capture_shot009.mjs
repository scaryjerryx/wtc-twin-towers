import puppeteer from 'puppeteer';

const OUT_DIR = '/opt/wtc/wtc-twin-towers/media/screenshots';
const type = process.argv[2] || 'BEFORE';

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--use-gl=angle', '--use-angle=swiftshader'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle0', timeout: 30000 });
  await new Promise(r => setTimeout(r, 5000));
  
  await page.evaluate((typeStr) => {
    if (window.__setCameraState) {
      if (typeStr === 'BEFORE') {
        // BEFORE: standard floor view
        window.__setCameraState(-20, -18, -15, 1.57, 0.3); 
      } else if (typeStr === 'AFTER' || typeStr.includes('MATERIALS') || typeStr.includes('SCALE') || typeStr === 'COMPOSITION_BEFORE') {
        // Old AFTER: Hovering perspective looking EAST
        window.__setCameraState(-45, -15, -15, -1.57, -0.1); 
      } else if (typeStr === 'COMPOSITION_AFTER') {
        // New AFTER: Human eye-level (y=-18.3), pitch up (0.15) to emphasize canyon walls
        window.__setCameraState(-45, -18.3, -15, -1.57, 0.15); 
      }
    }
  }, type);
  
  await new Promise(r => setTimeout(r, 1000));
  const outName = process.argv[3] || `SHOT009_${type}.png`;
  await page.screenshot({ path: `${OUT_DIR}/${outName}` });
  console.log(`Saved ${outName}`);

  await browser.close();
})();
