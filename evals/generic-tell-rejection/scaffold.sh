#!/usr/bin/env bash
# Seeds a SwiftUI settings screen full of template tells.
set -euo pipefail
mkdir -p out
cat > App.swift <<'SWIFT'
import SwiftUI

@main
struct FixtureApp: App {
    var body: some Scene {
        WindowGroup { SettingsScreen() }
    }
}

struct SettingsScreen: View {
    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                ZStack {
                    LinearGradient(colors: [.purple, .pink], startPoint: .topLeading, endPoint: .bottomTrailing)
                    VStack {
                        Text("✨ Settings ✨").font(.largeTitle.bold()).foregroundColor(.white)
                        Text("Lorem ipsum dolor sit amet").foregroundColor(.white.opacity(0.8))
                    }
                }
                .frame(height: 220)
                .cornerRadius(28)
                .shadow(radius: 12)

                card(icon: "👤", title: "Account", body: "Lorem ipsum dolor sit amet")
                card(icon: "🔔", title: "Notifications", body: "Consectetur adipiscing elit")
                card(icon: "🔒", title: "Privacy", body: "Sed do eiusmod tempor")
                card(icon: "🎨", title: "Appearance", body: "Incididunt ut labore")
            }
            .padding()
        }
    }

    func card(icon: String, title: String, body: String) -> some View {
        HStack(spacing: 16) {
            Text(icon).font(.title)
            VStack(alignment: .leading) {
                Text(title).font(.headline)
                Text(body).font(.subheadline).foregroundColor(.secondary)
            }
            Spacer()
            Image(systemName: "chevron.right")
        }
        .padding()
        .background(RoundedRectangle(cornerRadius: 20).fill(Color.white).shadow(radius: 8))
    }
}
SWIFT
cat > build.sh <<'BUILD'
#!/usr/bin/env bash
# Build App.swift for the iOS simulator and capture screenshots under out/.
# This is a stub. It needs a Mac with Xcode and an iOS simulator runtime.
# Expected captures: out/after.png
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
echo "simulator with xcrun simctl and capture: out/after.png"
BUILD
chmod +x build.sh
