# Autonomous Command Allowlist 001

## Workflow Command Diagnostic

Here are the shell commands used during the reconstruction workflow:

### 1. `npm run dev`
* **Purpose:** Starts the local Vite development server required for rendering the Three.js/React Three Fiber engine.
* **Frequency:** Once per session (runs continuously in the background).
* **Safe to auto-approve:** **YES**

### 2. `npm run build`
* **Purpose:** Compiles TypeScript and builds the frontend production bundle to ensure no typing or syntax errors exist before capture.
* **Frequency:** Once per iteration.
* **Safe to auto-approve:** **YES**

### 3. `node capture_shot*.mjs`
* **Purpose:** Executes Puppeteer headless browser scripts to capture high-resolution screenshots of the engine output for validation.
* **Frequency:** Once per iteration.
* **Safe to auto-approve:** **YES**

### 4. `find src -type f` / `grep`
* **Purpose:** File discovery and locating target React components (`.tsx`) for scene modification.
* **Frequency:** 1-2 times per iteration.
* **Safe to auto-approve:** **YES**

### 5. `git diff` / `git status`
* **Purpose:** Validates the scope of file modifications prior to finalizing an iteration.
* **Frequency:** High (multiple times per iteration).
* **Safe to auto-approve:** **YES**

### 6. `npm run test` (or Validation Scripts)
* **Purpose:** Runs local test suites or static validation checks.
* **Frequency:** Once per iteration.
* **Safe to auto-approve:** **YES**

---

## Minimum Required Allowlist

To eliminate command approval interruptions while preserving safety, add the following commands to your extension's **Allowed Commands** (Auto-Approve) configuration:

```json
[
  "npm run dev",
  "npm run build",
  "node capture_shot*",
  "find src",
  "git diff",
  "git status"
]
```
