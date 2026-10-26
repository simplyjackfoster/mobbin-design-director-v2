Fixture response. These two flows are eval fixtures, not real Mobbin captures. The apps and URLs do not exist.

```json
{
  "fixture": true,
  "results": [
    {
      "id": "fixture-flow-0001",
      "app_name": "Fixture Pay",
      "platform": "ios",
      "flow_title": "Add a card issuer",
      "actions": ["Selecting", "Reviewing", "Confirming"],
      "screen_count": 8,
      "preview_positions": [1, 5, 8],
      "mobbin_url": "https://mobbin.com/flows/fixture-flow-0001",
      "screens": [
        {"position": 1, "title": "Issuer list", "image_url": "https://fixtures.invalid/mobbin/fixture-flow-0001-1.webp"},
        {"position": 5, "title": "Review", "image_url": "https://fixtures.invalid/mobbin/fixture-flow-0001-5.webp"},
        {"position": 8, "title": "Success", "image_url": "https://fixtures.invalid/mobbin/fixture-flow-0001-8.webp"}
      ]
    },
    {
      "id": "fixture-flow-0002",
      "app_name": "Fixture Bank",
      "platform": "ios",
      "flow_title": "Link an account",
      "actions": ["Searching", "Selecting", "Logging in"],
      "screen_count": 6,
      "preview_positions": [1, 3, 6],
      "mobbin_url": "https://mobbin.com/flows/fixture-flow-0002",
      "screens": [
        {"position": 1, "title": "Search institutions", "image_url": "https://fixtures.invalid/mobbin/fixture-flow-0002-1.webp"},
        {"position": 3, "title": "Credentials", "image_url": "https://fixtures.invalid/mobbin/fixture-flow-0002-3.webp"},
        {"position": 6, "title": "Linked", "image_url": "https://fixtures.invalid/mobbin/fixture-flow-0002-6.webp"}
      ]
    }
  ],
  "ai_usage_notice": "Fixture notice. Cite mobbin_url for each reference. Image URLs expire."
}
```
