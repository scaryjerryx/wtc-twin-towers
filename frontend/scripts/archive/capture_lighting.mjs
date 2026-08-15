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
  
  await page.evaluate(() => {
    if (window.__setCameraState) {
      // Angle looking up at the West wall to see shadows from the tie-backs
      window.__setCameraState(-40, -10, -25, 0.5, 0.4); 
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/BATHTUB_LIGHTING_${type}.png` });
  console.log(`Saved BATHTUB_LIGHTING_${type}.png`);

  await browser.close();
})();
