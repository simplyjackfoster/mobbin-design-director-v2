#!/usr/bin/env bash
# Seeds a screen with hard-coded colors that break in dark mode.
set -euo pipefail
mkdir -p out
cat > App.swift <<'SWIFT'
import SwiftUI

@main
struct FixtureApp: App {
    var body: some Scene {
        WindowGroup { PlanCardScreen() }
    }
}

struct PlanCardScreen: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Roam Plus").font(.title2.bold()).foregroundColor(.black)
            Text("10 GB for 30 days").foregroundColor(Color(white: 0.35))
            Text("$24.00 total").font(.headline).foregroundColor(.black)
            Button(action: {}) {
                Text("Choose").foregroundColor(.white).frame(maxWidth: .infinity)
            }
            .padding()
            .background(Color.white)
        }
        .padding()
        .background(Color.white)
        .cornerRadius(12)
        .padding()
    }
}
SWIFT
cat > build.sh <<'BUILD'
#!/usr/bin/env bash
# Build App.swift for the iOS simulator and capture screenshots under out/.
# This is a stub. It needs a Mac with Xcode and an iOS simulator runtime.
# Expected captures: out/light.png out/dark.png
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
echo "simulator with xcrun simctl and capture: out/light.png out/dark.png"
BUILD
chmod +x build.sh
