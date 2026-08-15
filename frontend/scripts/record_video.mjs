import puppeteer from 'puppeteer';
import { execSync } from 'child_process';
import fs from 'fs';

(async () => {
  const artifactDir = '/root/.gemini/antigravity-cli/brain/4440caf0-0c94-4d4b-b550-7a17abeb5efd';
  const framesDir = `${artifactDir}/scratch/frames`;
  const videoPath = `${artifactDir}/atmosphere_walkthrough_001.mp4`;
  const screen1 = `${artifactDir}/screenshot_spawn.png`;
  const screen2 = `${artifactDir}/screenshot_trailer_interior.png`;
  const screen3 = `${artifactDir}/screenshot_inspect_drawing.png`;

  if (!fs.existsSync(framesDir)) {
    fs.mkdirSync(framesDir, { recursive: true });
  } else {
    fs.rmSync(framesDir, { recursive: true, force: true });
    fs.mkdirSync(framesDir, { recursive: true });
  }

  console.log('Launching headless browser...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--use-gl=angle',
      '--use-angle=swiftshader',
      '--enable-webgl',
      '--ignore-gpu-blocklist'
    ]
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  
  console.log('Navigating to http://localhost:5173/ ...');
  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle0', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));

  // Spawn screenshot
  await page.screenshot({ path: screen1 });

  const fps = 30;
  const walkFrames = 90;
  
  console.log('Recording walk...');
  // Walk from spawn (0, 1.7, 10) to trailer entrance (5.5, 1.7, -1)
  for (let i = 0; i <= walkFrames; i++) {
    const p = i / walkFrames;
    const x = 0 + (7 * p);
    const z = 10 + (-10 * p);
    // Face the trailer
    const yaw = -0.3; // Look slightly left
    
    await page.evaluate((px, py, pz, pyaw) => {
      if (window.__setCameraState) {
        window.__setCameraState(px, py, pz, pyaw, 0);
      }
    }, x, 1.7, z, yaw);
    
    await new Promise(r => setTimeout(r, 50));
    
    const frameNum = String(i).padStart(5, '0');
    await page.screenshot({ path: `${framesDir}/frame_${frameNum}.png` });
  }

  // Inside trailer screenshot
  await page.screenshot({ path: screen2 });

  // Walk into trailer to look at drawing (10, 1.7, -2) is center, table is (10, 0.85, -2)
  console.log('Recording trailer entry...');
  const trailerFrames = 40;
  for (let i = 1; i <= trailerFrames; i++) {
    const p = i / trailerFrames;
    const x = 7 + (1 * p); // Step in
    const z = 0 + (-1.5 * p); // Step forward
    const yaw = -0.3 + (0.3 * p); // Turn right to face table
    const pitch = 0 - (0.3 * p); // Look down
    
    await page.evaluate((px, py, pz, pyaw, ppitch) => {
      if (window.__setCameraState) {
        window.__setCameraState(px, py, pz, pyaw, ppitch);
      }
    }, x, 1.7, z, yaw, pitch);
    
    await new Promise(r => setTimeout(r, 50));
    
    const frameNum = String(walkFrames + i).padStart(5, '0');
    await page.screenshot({ path: `${framesDir}/frame_${frameNum}.png` });
  }

  console.log('Triggering interaction...');
  await page.evaluate(() => {
    if (window.__triggerDrawingS1) {
      window.__triggerDrawingS1();
    }
  });

  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: screen3 });

  // Hold for a few frames
  for (let i = 1; i <= 30; i++) {
    const frameNum = String(walkFrames + trailerFrames + i).padStart(5, '0');
    await page.screenshot({ path: `${framesDir}/frame_${frameNum}.png` });
  }

  await browser.close();

  console.log('Generating video with ffmpeg...');
  execSync(`ffmpeg -y -framerate ${fps} -i ${framesDir}/frame_%05d.png -c:v libx264 -pix_fmt yuv420p ${videoPath}`);
  console.log('Video saved to: ' + videoPath);

})().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
