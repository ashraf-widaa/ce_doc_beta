/* Optional capture utility. Not a Sphinx/RTD build dependency.
 * Requires Playwright + Chromium. Uses public built-in data, never submits feedback.
 * Usage: node scripts/docs/capture_browser_examples.cjs OUTPUT_DIRECTORY
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const output = path.resolve(process.argv[2] || 'browser-captures');
  fs.mkdirSync(output, { recursive: true });
  const launch = { headless: true };
  if (process.env.CE_CHROMIUM_EXECUTABLE) launch.executablePath = process.env.CE_CHROMIUM_EXECUTABLE;
  const browser = await chromium.launch(launch);
  try {
    const page = await browser.newPage({
      viewport: { width: 1440, height: 1000 },
      ignoreHTTPSErrors: process.env.CE_BROWSER_IGNORE_TLS_ERRORS === '1',
    });
    await page.goto('https://calibrated-explanations-demo.ju.se/expert', { waitUntil: 'domcontentloaded' });
    await page.getByRole('button', { name: /Diabetes \(Binary Classification\)/ }).click();
    await page.getByRole('button', { name: 'Next: Prepare & Calibrate', exact: true }).click();
    await page.getByRole('button', { name: 'Prepare Random Forest + Calibrate', exact: true }).click();
    await page.getByText('Calibrated', { exact: true }).first().waitFor({ timeout: 90000 });
    await page.getByRole('button', { name: 'Next: Explain', exact: true }).click();
    await page.locator('tbody tr').first().click();
    await page.getByText('Factual Explanation Plot', { exact: true }).waitFor({ timeout: 60000 });
    const feedback = page.getByRole('button', { name: 'Not now', exact: true });
    if (await feedback.isVisible()) await feedback.click();
    await page.waitForTimeout(750);
    const bodyText = await page.locator('body').innerText();
    fs.writeFileSync(path.join(output, 'expert-factual.txt'), bodyText);
    const handle = await page.getByText('Instance #0', { exact: true }).evaluateHandle(element => {
      for (let node = element; node; node = node.parentElement) {
        if (node.innerText.includes('Factual Explanation Plot') && !node.innerText.includes('Test Set Instances')) return node;
      }
      throw new Error('Cannot identify the real explanation panel; no substitute image created.');
    });
    await handle.asElement().screenshot({ path: path.join(output, 'expert-factual-focus.png') });
    fs.writeFileSync(path.join(output, 'capture-manifest.json'), JSON.stringify({
      capturedAt: new Date().toISOString(), url: page.url(), dataset: 'Diabetes (Binary Classification)',
      query: 'Test Set Instances row 0', viewport: { width: 1440, height: 1000 },
      method: 'Unmodified screenshot of the actual explanation panel; no synthetic UI or values',
      note: 'Recheck values, labels and associated prose before replacing published assets.',
    }, null, 2));
    console.log('Captured actual factual panel and provenance. Check associated text before reuse.');
  } finally { await browser.close(); }
})().catch(error => { console.error(error.message); process.exitCode = 1; });
