import { copyFile, mkdir, stat } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const source = path.join(root, "raw", "SkillsMemoryDashboard.html")
const target = path.join(root, "content", "SkillsMemoryDashboard.html")

await stat(source)
await mkdir(path.dirname(target), { recursive: true })
await copyFile(source, target)

console.log(`Synced ${path.relative(root, source)} -> ${path.relative(root, target)}`)
