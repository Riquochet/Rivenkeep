# Rivenkeep — Developer Setup Guide
**For:** Jack (macOS, IntelliJ/Windsurf user, new to Xcode/Swift)
**Date:** 2026-04-04

---

## Step 1: Install Xcode (30-60 min, mostly waiting)

Xcode is Apple's IDE. We only need it to build and run on the iPhone simulator. All actual coding happens in IntelliJ/Windsurf.

1. Open the **App Store** on your Mac (the blue "A" icon in the dock or spotlight search "App Store")
2. Search for **"Xcode"** — it's by Apple, has a hammer icon
3. Click **Get / Install** — it's free but HUGE (~35 GB download). Start this before bed or during a meeting.
4. Wait. This is the longest step. Go make coffee.
5. Once installed, **open Xcode once** — it will ask to install "Additional Components." Click **Install**. Enter your Mac password. Wait 5 more minutes.
6. Agree to the license agreement when prompted.

**Verify it worked:** Open Terminal (Spotlight → type "Terminal") and run:
```
xcode-select --version
```
You should see a version number. If you see an error, run:
```
xcode-select --install
```

### Install the iPhone Simulator

Xcode ships with simulators, but you may need to download one:

1. Open **Xcode**
2. Menu bar: **Xcode → Settings** (or ⌘,)
3. Click the **Platforms** tab
4. You should see "iOS 18.x" (or whatever the latest is). If not, click the **+** button at bottom-left and add **iOS**
5. This downloads another ~5-7 GB. Wait again.

**Test the simulator:** 
1. In Xcode, menu: **Xcode → Open Developer Tool → Simulator**
2. An iPhone should appear on screen. If it boots to a home screen, you're good.
3. Close the Simulator for now.

---

## Step 2: Install Claude Code CLI (5 min)

Claude Code lets me read and write files directly in your project directory. You talk to me in your terminal instead of this chat window.

**Requirements:** Your Claude.ai account must be Pro, Max, Teams, or Enterprise. The free plan doesn't include Claude Code.

1. Open **Terminal**
2. Run this one command:
```bash
curl -fsSL https://claude.ai/install.sh | sh
```
3. It downloads and installs the binary to `~/.local/bin/claude`
4. **Close Terminal and open a new one** (so your PATH updates)
5. Verify:
```bash
claude --version
```
You should see a version number.

6. First-time auth — run:
```bash
claude
```
This opens your browser to Anthropic's login. Sign in with your Claude account. Authorize the CLI. Done.

7. To quit Claude Code, type `/exit` or Ctrl+C.

### How Claude Code works with your project

```bash
cd ~/Projects/RivenkeepGame    # navigate to your project
claude                          # start Claude Code in that directory
```

Now Claude can read every file in that directory and write new ones directly. You say "create Grid.swift with the 48x64 grid system" and it writes the file to disk. You say "read BattleScene.swift and fix the enclosure bug" and it reads your actual code.

**Important for your workflow:** You can have Claude Code running in one terminal tab AND this Claude.ai chat open in a browser tab simultaneously. Use Claude.ai (here) for design discussions, GDD work, and big-picture architecture. Use Claude Code for "write this file" and "fix this bug" in your actual project directory.

---

## Step 3: Create the Xcode Project (10 min)

This creates the project skeleton that Xcode builds and the simulator runs.

1. Open **Xcode**
2. Click **"Create New Project"** (or File → New → Project)
3. Choose **iOS** at the top
4. Select **"Game"** template → click **Next**
5. Fill in:
   - **Product Name:** `RivenkeepGame`
   - **Team:** Your personal team (if you don't have one, click "Add Account" and sign in with your Apple ID — a free account works for simulator)
   - **Organization Identifier:** `com.yourname` (e.g., `com.jackdev`)
   - **Language:** **Swift**
   - **Game Technology:** **SpriteKit**
   - Uncheck "Include Tests" for now (we'll add them manually later)
6. Click **Next**
7. Save it to: `~/Projects/RivenkeepGame` (create the Projects folder if needed)
8. Click **Create**

Xcode opens with your new project. You'll see a bunch of files it generated.

### Run it on the Simulator

1. At the top of Xcode, there's a device selector (probably says "iPhone 16" or similar). Click it and pick any iPhone model.
2. Click the **▶ Play button** (top-left) or press **⌘R**
3. The simulator launches with a gray screen showing "Hello, World!" and a rotating spaceship sprite
4. If you see the spaceship spinning, **your environment is working**
5. Press **⌘.** (Command + Period) to stop the simulator

### Delete the template junk

The template creates files we don't need. In Xcode's left sidebar (file navigator):
1. Right-click `GameScene.sks` → **Delete** → **Move to Trash**
2. Right-click `Actions.sks` → **Delete** → **Move to Trash**
3. Leave `GameScene.swift`, `GameViewController.swift`, `AppDelegate.swift` — we'll replace their contents later

---

## Step 4: Set Up the Project Structure (5 min)

In Terminal (or IntelliJ/Windsurf file browser):

```bash
cd ~/Projects/RivenkeepGame/RivenkeepGame

# Core logic (pure Swift, no SpriteKit)
mkdir Core

# SpriteKit scenes
mkdir Scenes

# SpriteKit visual nodes
mkdir Nodes

# Audio and haptics
mkdir Audio
mkdir Haptics

# Data files (JSON maps, overlays, campaigns)
mkdir Data

# Tests
cd ..
mkdir RivenkeepGameTests
```

Your project folder should now look like:
```
RivenkeepGame/
├── RivenkeepGame.xcodeproj     ← Xcode project file
├── RivenkeepGame/
│   ├── AppDelegate.swift
│   ├── GameViewController.swift
│   ├── GameScene.swift
│   ├── Assets.xcassets/
│   ├── Core/                   ← Pure game logic (NEW)
│   ├── Scenes/                 ← SpriteKit scenes (NEW)
│   ├── Nodes/                  ← Visual components (NEW)
│   ├── Audio/                  ← Sound manager (NEW)
│   ├── Haptics/                ← Haptic patterns (NEW)
│   └── Data/                   ← JSON data files (NEW)
└── RivenkeepGameTests/         ← Unit tests (NEW)
```

### Tell Xcode about the new folders

Xcode needs to know about folders you created outside of it:
1. In Xcode's left sidebar, right-click the **"RivenkeepGame"** folder (yellow icon)
2. Select **"Add Files to RivenkeepGame..."**
3. Navigate to the `Core` folder, select it, make sure "Create groups" is selected → **Add**
4. Repeat for `Scenes`, `Nodes`, `Audio`, `Haptics`, `Data`
5. The folders now appear in Xcode's sidebar with yellow folder icons

---

## Step 5: Configure for iPhone Portrait Only (2 min)

1. In Xcode's left sidebar, click the **top-level "RivenkeepGame"** project (blue icon at very top)
2. Under **Targets**, click **"RivenkeepGame"**
3. Click the **General** tab
4. Scroll to **"Deployment Info"**:
   - **iOS Deployment Target:** Set to `16.0` (supports iPhone 8 and newer)
   - Under **Supported Destinations**, make sure **iPhone** is checked
5. Scroll to **"Device Orientation"**:
   - Check **Portrait** only
   - Uncheck Landscape Left and Landscape Right
   - Uncheck Upside Down

---

## Step 6: Verify Everything Works (2 min)

1. Press **⌘R** to build and run on the simulator
2. You should see the template game screen in portrait mode
3. If it builds and runs: **you're ready to code**

---

## Your Daily Workflow

```
Morning/Day (work hours):
  → Claude.ai browser: GDD refinement, UI design, analysis threads

Evening/Weekend (personal time):
  → Open IntelliJ/Windsurf with ~/Projects/RivenkeepGame
  → Open Terminal, cd to project, run: claude
  → Tell Claude Code what to build: "Create Core/Grid.swift with..."
  → Claude Code writes the file directly to your project
  → Switch to Xcode, press ⌘R to build and test on simulator
  → Report bugs/issues to Claude Code, iterate
  
  OR
  
  → Open Claude.ai, upload files, discuss architecture
  → Download generated files, place in project
  → Build in Xcode
```

### IntelliJ/Windsurf Setup for Swift

IntelliJ can edit Swift files with syntax highlighting:
1. Open IntelliJ → **Settings → Plugins → Marketplace**
2. Search for **"Swift"** — install the Swift plugin if available
3. Open the `~/Projects/RivenkeepGame` folder as a project
4. Edit `.swift` files with syntax highlighting
5. Build/run happens in Xcode (⌘-tab to switch)

Windsurf handles Swift natively — just open the project folder.

---

## What's Next

Once you've completed all 6 steps and see the template running on the simulator, come back to any conversation and say:

**"Xcode is set up, simulator works, targeting iOS 16. Let's start Grid.swift."**

That's our first coding session. I'll generate the complete `Grid.swift` file (the 48×64 game board with cell types, adjacency, and coordinate math) plus `GridTests.swift` to verify it. You paste them into the project, run tests, and we're building a game.
