#!/usr/bin/env bash
# Seeds a screen with icon-only buttons and an unlabeled decorative image.
set -euo pipefail
cat > App.swift <<'SWIFT'
import SwiftUI

@main
struct FixtureApp: App {
    var body: some Scene {
        WindowGroup { BookDetailScreen() }
    }
}

struct BookDetailScreen: View {
    @State private var saved = false
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Image(systemName: "sparkles")
                .font(.system(size: 64))
                .frame(maxWidth: .infinity)
            Text("Morning Light").font(.title.bold())
            Text("Mira Chen").foregroundColor(.secondary)
            HStack(spacing: 24) {
                Button(action: { saved.toggle() }) {
                    Image(systemName: saved ? "bookmark.fill" : "bookmark")
                }
                Button(action: {}) {
                    Image(systemName: "square.and.arrow.up")
                }
                Button(action: {}) {
                    Image(systemName: "ellipsis")
                }
            }
            .font(.title2)
            Spacer()
        }
        .padding()
    }
}
SWIFT
