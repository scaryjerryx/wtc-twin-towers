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
  
  // 1. BATHTUB_WIDE (From street level looking down into the massive crater)
  await page.evaluate(() => {
    if (window.__setCameraState) {
      window.__setCameraState(0, 1.7, 10, 0.78, -0.4); // Looking down and left toward the pit center
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/BATHTUB_WIDE.png` });
  console.log('Saved BATHTUB_WIDE.png');

  // 2. BATHTUB_FLOOR (From the bedrock floor looking up at the walls)
  await page.evaluate(() => {
    if (window.__setCameraState) {
      // Move to the pit floor (Y = -18), looking up at the west wall
      window.__setCameraState(-20, -18, -15, 1.57, 0.3); 
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/BATHTUB_FLOOR.png` });
  console.log('Saved BATHTUB_FLOOR.png');

  // 3. BATHTUB_WALL_DETAIL (Zoomed in on the panel seams and tie-back anchors)
  await page.evaluate(() => {
    if (window.__setCameraState) {
      // Move close to the North Wall tie-backs
      window.__setCameraState(-25, -10, -30, 0, 0.2); 
    }
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: `${OUT_DIR}/BATHTUB_WALL_DETAIL.png` });
  console.log('Saved BATHTUB_WALL_DETAIL.png');

  await browser.close();
})();
