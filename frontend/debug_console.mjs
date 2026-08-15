import puppeteer from 'puppeteer';

(async () => {
  console.log('--- STARTING BROWSER DIAGNOSTICS ---');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();

  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.type(), msg.text()));
  page.on('pageerror', err => console.error('BROWSER UNCAUGHT ERROR:', err.message));
  page.on('requestfailed', req => console.error('REQUEST FAILED:', req.url(), req.failure()?.errorText));

  await page.goto('http://localhost:5173/', { waitUntil: 'networkidle0', timeout: 15000 });
  
  await browser.close();
  console.log('--- END DIAGNOSTICS ---');
})().catch(err => console.error('Diagnostic Script Error:', err));
