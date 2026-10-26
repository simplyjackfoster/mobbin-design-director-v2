# iOS writing and alerts

Read this when you write a label, a button, an alert, an error, an empty state, or onboarding copy for an iPhone screen.

## Casing: what the HIG says

The HIG does not mandate sentence case. It says: "Title case is generally considered formal, while sentence case is more casual. Choose a style for each UI element type and use it consistently." So the rule is one casing style per element type. Buttons and alert buttons are title case. Menu items are title case. A brief that says "sentence case everywhere" is wrong for iOS. Source: https://developer.apple.com/design/human-interface-guidelines/writing , https://developer.apple.com/design/human-interface-guidelines/alerts , https://developer.apple.com/design/human-interface-guidelines/menus

## Writing rules

From the HIG Writing page: https://developer.apple.com/design/human-interface-guidelines/writing (markdown mirror: https://developer.apple.com/tutorials/data/design/human-interface-guidelines/writing.md)

1. Buttons and links: "it's almost always best to use a verb". "Send" beats "Let's do it!".
2. Never write "Click here". Use a descriptive phrase.
3. Casing: choose one style per UI element type and use it consistently. Title case is "generally considered formal", sentence case is "more casual".
4. Avoid "we". "Unable to load content" beats "We're having trouble loading this content."
5. Use possessives sparingly. "Favorites", not "Your Favorites".
6. Errors say how to fix. "Choose a password with at least 8 characters" beats "That password is too short." No "oops!" and no "uh-oh". They "can sound insincere".
7. Field errors sit next to the field and do not scold. "Use only letters for your name" beats "Don't use numbers or symbols". Never "Invalid name".
8. Settings describe the on state only.
9. Flows: "Get Started" to begin, "Continue" or "Next" used consistently, "Done" to end.
10. Empty states give the next action and a button.
11. Match tone to context. The HIG contrasts fall detection with a Move streak.

## Alert rules

From the HIG Alerts page: https://developer.apple.com/design/human-interface-guidelines/alerts

12. Title: a complete sentence takes sentence case and end punctuation. A fragment takes title case and no punctuation. Never "Error".
13. Buttons: title case, no punctuation, verbs ("View All", "Reply", "Ignore"). "OK" only in an informational alert. Never "Yes" or "No". Always "Cancel" for cancel. Cancel is never the default. A single button alert uses "Done".
14. Destructive style only when the person did not deliberately choose the action.
15. No alert for a common undoable delete. Use an action sheet for choices about an intentional action.

## Buttons

Start the label with a verb. Title style capitalization. 44x44 pt hit region. Source: https://developer.apple.com/design/human-interface-guidelines/buttons

## Tone

Mailchimp: "Our voice doesn't change much ... but our tone changes all the time". It is "always more important to be clear than entertaining". "Don't go out of your way to make a joke." Source: https://styleguide.mailchimp.com/voice-and-tone/

## AI copy tells

Copy that reads as generated. The sourcing is uneven, so each item says where it stands.

- Exclamation marks. Unsourced. The research found no source for this tell.
- "Welcome back, Alex!" and other greeting lines. Unsourced. The research found no source for this tell.
- Marketing voice in product UI. Hero clichés such as "Build the future of work" "means nothing". "A frequent-use work surface uses promotional spacing". Sourced: https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c , https://thecrit.co/resources/does-your-ai-built-app-look-vibe-coded
- Title Case everywhere, em dashes, and "seamlessly". Sourced: https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md , https://www.adriankrebs.ch/blog/design-slop/

Read the Title Case tell with the casing rule above. The tell is title case applied without a decision, across body text, headings, and labels alike. On iOS, buttons, alert buttons, and menu items are title case by rule. That is a decision, not a tell.

No named author critique of AI sounding UI copy was found. The only hit was an NN/g video: https://www.nngroup.com/videos/ai-for-tone/
