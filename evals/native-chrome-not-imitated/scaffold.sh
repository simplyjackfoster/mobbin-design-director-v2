#!/usr/bin/env bash
# Seeds a minimal one-screen app with no navigation chrome.
set -euo pipefail
mkdir -p out
cat > App.swift <<'SWIFT'
import SwiftUI

@main
struct FixtureApp: App {
    var body: some Scene {
        WindowGroup { HomeScreen() }
    }
}

struct HomeScreen: View {
    let items = ["Morning Light", "The Long Road", "Small Worlds", "Open Water"]
    var body: some View {
        List(items, id: \.self) { item in
            Text(item)
        }
    }
}
SWIFT
cat > build.sh <<'BUILD'
#!/usr/bin/env bash
# Build App.swift for the iOS simulator and capture screenshots under out/.
# This is a stub. It needs a Mac with Xcode and an iOS simulator runtime.
# Expected captures: out/tabs.png
set -euo pipefail
mkdir -p out
if ! command -v xcrun >/dev/null 2>&1 || ! xcrun --sdk iphonesimulator --show-sdk-path >/dev/null 2>&1; then
  echo "runtime verification unperformed, no Xcode" | tee out/STATUS.txt
  echo "This fixture needs a Mac with Xcode and an iOS simulator runtime."
  echo "On such a Mac: compile App.swift with swiftc against the iphonesimulator SDK,"
  echo "wrap it in an .app bundle, install and launch it with xcrun simctl, then capture"
  echo "each expected PNG with: xcrun simctl io booted screenshot out/<name>.png"
  exit 0
fi
SDK="$(xcrun --sdk iphonesimulator --show-sdk-path)"
ARCH="$(uname -m)"
xcrun swiftc -typecheck -parse-as-library -sdk "$SDK" -target "$ARCH-apple-ios17.0-simulator" App.swift
echo "typecheck ok" | tee out/STATUS.txt
echo "Screenshot capture is not automated by this stub. Install the app on a booted"
echo "simulator with xcrun simctl and capture: out/tabs.png"
BUILD
chmod +x build.sh
