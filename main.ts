import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync("entry.png", dest);
const written = statSync(dest).size;
const source = statSync("entry.png").size;
if (written !== source) {
  throw new Error(`size mismatch: wrote ${written}, source is ${source}`);
}
console.log(`wrote ${dest} (${written} bytes)`);
