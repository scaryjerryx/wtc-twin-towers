import puppeteer from 'puppeteer';
import path from 'path';

const OUT_DIR = '/opt/wtc/wtc-twin-towers/media/screenshots';

(async () => {
  console.log('Launching headless browser...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--use-gl=angle', '--use-angle=swiftshader'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });

  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));

  console.log('Navigating to http://localhost:5173/ ...');
  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle0', timeout: 30000 });

  await new Promise(r => setTimeout(r, 5000));
  
  // 1. PATH_TUBE_FROM_SPAWN
  await page.evaluate(() => {
    if (window.__setCameraState) {
      window.__setCameraState(0, 1.7, 10, 0.78, -0.2); // Look left from spawn towards the pit
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/PATH_TUBE_FROM_SPAWN.png` });
  console.log('Saved PATH_TUBE_FROM_SPAWN.png');

  // 2. PATH_TUBE_WIDE
  await page.evaluate(() => {
    if (window.__setCameraState) {
      // Move to the far side of the pit, looking back at the tube crossing it
      window.__setCameraState(-35, 1.7, -5, -1.0, -0.1); 
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/PATH_TUBE_WIDE.png` });
  console.log('Saved PATH_TUBE_WIDE.png');

  // 3. PATH_TUBE_CLOSEUP
  await page.evaluate(() => {
    if (window.__setCameraState) {
      // Move right next to the tube's support trusses in the pit
      window.__setCameraState(-20, -5, -10, 0, 0.2); 
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/PATH_TUBE_CLOSEUP.png` });
  console.log('Saved PATH_TUBE_CLOSEUP.png');

  await browser.close();
})();
