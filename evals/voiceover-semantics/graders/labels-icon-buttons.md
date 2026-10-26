---
type: regex
target:
  source: file
  path: App.swift
pattern: "(?:accessibilityLabel[\\s\\S]*?){3}|(?:Label\\([\\s\\S]*?systemImage:[\\s\\S]*?){3}"
weight: 2
---
