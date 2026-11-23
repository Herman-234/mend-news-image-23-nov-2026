// news-image-20261123 entry (Node 22, standard library only).
// The poster beside this file is the whole entry: copy it to the
// output directory. The grader runs this twice with no network and
// both runs must write identical bytes, so this is a plain byte
// copy and nothing else — no dates, no randomness, no I/O besides
// the single copy.
//
// Run locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, statSync } from "node:fs";
import { join } from "node:path";

const entryPath = new URL("./entry.png", import.meta.url).pathname;
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

if (!existsSync(entryPath)) {
  throw new Error("entry.png is missing next to main.ts");
}
if (statSync(entryPath).size > 1048576) {
  throw new Error("entry.png is over the 1 MiB gate limit");
}
copyFileSync(entryPath, join(outDir, "entry.png"));
