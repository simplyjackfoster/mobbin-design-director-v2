---
type: regex
target:
  source: file
  path: App.swift
pattern: "RoundedRectangle[\\s\\S]{0,200}frame\\(height:\\s*(49|83|8[0-9])\\)|frame\\(height:\\s*(49|83)\\)"
match: not_contains
weight: 1
---
