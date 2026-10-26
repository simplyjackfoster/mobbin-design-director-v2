# Defaults detector

Read this when you review a web or iOS screen for choices that a tool made instead of a person.

**The rule.** Every choice that matches a known tool default needs a stated reason, or it changes. The tables list the tells that scanners and critics agree on. A tell is a prompt to decide, not a ban. [Visual](visual.md) holds the same position: diagnose a specific failure, do not ban a treatment.

## Web

| Tell | Why it reads as a default | Counter-move | Source |
|---|---|---|---|
| Purple to blue gradient on a hero, a CTA, or a clipped headline | Tailwind indigo and violet defaults. "VibeCode Purple". "the Times New Roman of AI-generated design" | One solid accent token. Ban the 250 to 280 hue range for a project | https://www.adriankrebs.ch/blog/design-slop/ , https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md |
| Inter or Geist everywhere. Space Grotesk plus one Instrument Serif italic accent word | Shipped when no font was chosen. Krebs detects the exact trio | A face with a point of view. No lone serif italic word | https://www.adriankrebs.ch/blog/design-slop/ , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md |
| Cream `#faf8f4` plus sage or terracotta. Near black plus acid green | Second order defaults. The fix for purple is now its own template. Anthropic flags "near-black background with a single bright acid-green or vermilion accent" | Keep a warm base. Choose an off-trend secondary. Vary value contrast | https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md , https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md , https://github.com/funboy322/avoid-ai-design |
| Grey body text (`gray-400` or `gray-500`) | An AI tell and a WCAG failure | Near black body. Grey for metadata only | https://www.adriankrebs.ch/blog/design-slop/ , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md |
| Glassmorphism plus neon glow | Glow "competes with content". Text on blur fails contrast | Opaque surfaces. One elevation ramp. Glass on one chrome element at most | https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui , https://smoothui.dev/blog/ai-design-slop |
| One corner radius everywhere | "When every element has identical corners, hierarchy disappears" | A radius scale. Some elements square | https://noqta.tn/en/blog/ai-design-slop-overused-ui-patterns-fix-2026 , https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c |
| Icon feature card, three in a row | "the most-generated component on earth" | Lead with a screenshot or a number. Drop the icon chip | https://www.adriankrebs.ch/blog/design-slop/ , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md , https://thecrit.co/resources/does-your-ai-built-app-look-vibe-coded |
| Coloured left or top border on cards | Krebs pattern 11. Kostac: "That damn left-edge coloured line". See the iOS row below for the one source that disagrees | Remove the stripe | https://www.adriankrebs.ch/blog/design-slop/ , https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c |
| Cards inside cards | Nothing ranks when everything is boxed | Whitespace and type to group. Cards only for actionable items | https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui , https://thecrit.co/resources/does-your-ai-built-app-look-vibe-coded |
| Pill badge above the hero H1. Sparkle icon for AI. Emoji as icons | Emoji "says the interface never needed to make a real decision about iconography" | The heading leads. One icon set | https://www.adriankrebs.ch/blog/design-slop/ , https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui , https://github.com/nutlope/hallmark |
| Codified section order. Three equal columns. Three or four stat tiles | "The sequence itself is the fingerprint" | Reorder around the argument. 7/5 splits. Stats inside the sections they belong to | https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md , https://www.adriankrebs.ch/blog/design-slop/ |
| Hero clichés, CTA clones, Title Case, em dashes, "seamlessly" | "Build the future of work" "means nothing" | Founder voice test. Sentence case. One claim, not three | https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md , https://www.adriankrebs.ch/blog/design-slop/ |
| Placeholder identities. Fabricated proof | "outcome claims without a nearby example" | Real odd numbers, or cut | https://thecrit.co/resources/does-your-ai-built-app-look-vibe-coded , https://github.com/claudiusararu/unslop-ui-skill/blob/main/TELLS.md |
| Marketing density on a work surface | "A frequent-use work surface uses promotional spacing" | Density matches use frequency | https://thecrit.co/resources/does-your-ai-built-app-look-vibe-coded |
| Missing empty, loading, and error states | "The happy path looks finished" | Design the highest consequence missing state first | https://thecrit.co/resources/does-your-ai-built-app-look-vibe-coded , https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c |
| Dashboard with no question | "there's no logic to it" | Start from the one question | https://kucharski.substack.com/p/ten-reasons-your-vibe-coded-dashboard |
| Every action a modal | Users "will refuse to give attention to further instances" | Inline edits. Sheets for transient actions | https://www.nngroup.com/articles/modal-nonmodal-dialog/ |
| Fade up on every element. Hover lift. Bounce everywhere | Anthropic calls fade and slide entrances "the generic default". Emil: "Avoid bounce in most UI contexts" | One reveal. Motion by role | https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md , https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md |
| One global `duration-300 ease-in-out`. Keyframes that restart. No reduced motion path | "Never use ease-in". "Keyframes restart from zero" | A timing scale. Transitions or springs. A reduced motion gate | https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md , https://github.com/nutlope/hallmark |

Community confirmation, one thread only: HN "Where's the AI design Renaissance?" says Lovable and v0 output "a Linear clone", that Figma Make and Claude Code "are really just using the out of the box CSS from shadcn", and that the result "looks 'designed' but there are obvious usability issues". Source: https://news.ycombinator.com/item?id=45602996

## iOS and SwiftUI

| Tell | Why it reads as a default | Counter-move | Source |
|---|---|---|---|
| Unstyled `List`, uniform `.body`, flat background. "indistinguishable from Apple's Settings app" | The tutorial default, reproduced | SF Pro design axes (`.serif` for prose, `.rounded` for numbers). A surface system | https://github.com/vermont42/iOS-Design-Agent-Skill |
| Settings as "one undifferentiated scroll" | No grouping decision was made | Group by task | https://github.com/vermont42/iOS-Design-Agent-Skill |
| `LinearGradient([.purple, .blue])`. A "Welcome to App" hero with big padding | A web landing page on a phone | Solid neutral. Small header, then content | https://github.com/wholiver/swiftui-design-skill |
| Symmetric three column grid | A web landing page on a phone | One featured card, smaller secondaries | https://github.com/wholiver/swiftui-design-skill |
| Emoji as icons. Inter or Roboto on Apple | Breaks the platform feel | SF Symbols. SF Pro or New York | https://github.com/wholiver/swiftui-design-skill |
| Rounded card with a left accent bar | Sources disagree. wholiver and Kostac call it the top tell. vermont42 prescribes it as the fix | Treat it as a tell. Separate with spacing and headers | https://github.com/wholiver/swiftui-design-skill , https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c , https://github.com/vermont42/iOS-Design-Agent-Skill |
| Fixed `.font(.system(size:))`. Overused `fontWeight()`. `onTapGesture` instead of `Button`. `GeometryReader` plus fixed frames | "All three popular LLMs seem to enjoy over-using the `fontWeight()` modifier" | Dynamic Type. Real buttons | https://www.hackingwithswift.com/articles/281/what-to-fix-in-ai-generated-swift-code |
| Default blue tint. Random spacing such as `.padding(13)` | "The agent has nothing in the project that says what your app looks like, so it guesses" | `.tint` at the root. 8 pt tokens. SwiftLint on raw values | https://github.com/wholiver/swiftui-design-skill , https://dev.to/nerd_snipe_dev/how-to-stop-your-ai-coding-agent-from-inventing-swiftui-ui-1km |

## How to use a hit

A detector hit is a diagnostic. Krebs reports "maybe" 5 to 10 percent false positives on 1,590 scored pages. Deterministic scanners (Krebs, avoid-ai-design `detect.mjs`, Hallmark gates) measure sameness, not quality. Quality comes from blind pairwise votes and from people. A stated direction is not a verified one: Design Theater found that more than 25 percent of stated design rationales never appear in the output. Scan, then look at the render. Sources: https://www.adriankrebs.ch/blog/design-slop/ , https://github.com/funboy322/avoid-ai-design , https://github.com/nutlope/hallmark , https://notes.designarena.ai/methodology/ , https://arxiv.org/abs/2607.22928

When you keep a hit, record the reason in the design packet. "The purple is the brand color, hex from the brand guide" is a reason. "It looked fine" is not.
