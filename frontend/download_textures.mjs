import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const baseDir = '/opt/wtc/wtc-twin-towers/frontend/public/textures';

async function downloadPolyhaven(id, outDir) {
  fs.mkdirSync(outDir, { recursive: true });
  const res = await fetch(`https://api.polyhaven.com/files/${id}`);
  const data = await res.json();
  const zipUrl = data.zip['2k'].url;
  console.log(`Downloading ${id} from ${zipUrl}`);
  execSync(`wget -qO temp.zip "${zipUrl}"`);
  execSync(`unzip -q temp.zip -d "${outDir}"`);
  execSync(`rm temp.zip`);
}

async function downloadAmbientCG(id, size, outDir) {
  fs.mkdirSync(outDir, { recursive: true });
  const url = `https://ambientcg.com/get?file=${id}_${size}-JPG.zip`;
  console.log(`Downloading ${id} from ${url}`);
  execSync(`wget -qO temp.zip "${url}"`);
  execSync(`unzip -q temp.zip -d "${outDir}"`);
  execSync(`rm temp.zip`);
}

async function main() {
  try {
    await downloadPolyhaven('brown_mud_02', path.join(baseDir, 'mud'));
    await downloadAmbientCG('Concrete015', '2K', path.join(baseDir, 'concrete'));
    await downloadPolyhaven('layered_rock', path.join(baseDir, 'bedrock'));
    await downloadAmbientCG('Metal035', '1K', path.join(baseDir, 'metal'));
    console.log("All textures downloaded and extracted.");
  } catch (err) {
    console.error(err);
  }
}
main();
