import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });

// Resolve entry.png from this file's own directory: the grader runs
// `node /bot/main.ts` from a working directory that is not the repo,
// so a relative "entry.png" would not be found there.
const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");
if (!existsSync(src)) {
  throw new Error(`entry.png not found next to main.ts: ${src}`);
}
const dest = join(outDir, "entry.png");
copyFileSync(src, dest);

const srcBytes = statSync(src).size;
const destBytes = statSync(dest).size;
if (srcBytes !== destBytes) {
  throw new Error(`copy mismatch: source ${srcBytes} bytes, wrote ${destBytes} bytes`);
}
console.log(`entry.png copied: ${destBytes} bytes to ${dest}`);
