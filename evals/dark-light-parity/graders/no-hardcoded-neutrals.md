---
type: regex
target:
  source: file
  path: App.swift
pattern: "foregroundColor\\(\\.black\\)|Color\\.white|Color\\(white:"
match: not_contains
weight: 2
---
