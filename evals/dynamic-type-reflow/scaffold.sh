#!/usr/bin/env bash
# Seeds a screen that clips at large Dynamic Type sizes.
set -euo pipefail
mkdir -p out
cat > App.swift <<'SWIFT'
import SwiftUI

@main
struct FixtureApp: App {
    var body: some Scene {
        WindowGroup { PlanSummaryScreen() }
    }
}

struct PlanSummaryScreen: View {
    var body: some View {
        VStack(spacing: 24) {
            Text("Roam Plus").font(.title2.bold())
            HStack(spacing: 12) {
                stat(value: "10 GB", label: "Data included for the trip")
                stat(value: "$24.00", label: "Total price, no top-up")
            }
            Spacer()
            Button(action: {}) {
                Text("Choose this plan")
                    .lineLimit(1)
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.borderedProminent)
            .frame(height: 56)
        }
        .padding()
    }

    func stat(value: String, label: String) -> some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(value).font(.title3.bold()).lineLimit(1)
            Text(label).font(.caption).foregroundColor(.secondary).lineLimit(1)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .frame(height: 64)
    }
}
SWIFT
cat > build.sh <<'BUILD'
#!/usr/bin/env bash
# Build App.swift for the iOS simulator and capture screenshots under out/.
# This is a stub. It needs a Mac with Xcode and an iOS simulator runtime.
# Expected captures: out/axxxl-before.png out/axxxl-after.png
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
echo "simulator with xcrun simctl and capture: out/axxxl-before.png out/axxxl-after.png"
BUILD
chmod +x build.sh
