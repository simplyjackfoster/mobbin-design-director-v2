# Worked examples: before and after

Read this when a brief resembles one of these jobs, or to see how the rules combine on one screen.

Each case: the job, a first draft with its tells in brackets from [defaults-detector](defaults-detector.md), the reasoning with the rule it applies, the revised design, and what a capture can verify per [evidence](evidence.md). "Hypothesis" marks a prediction, not a source.

## 1. Task capture: quick add with a date from Inbox

**Job**: A person on the Inbox list wants to add "Call the dentist" for tomorrow in a few seconds and keep scanning.

**Before**: A floating plus opens a full screen modal. Rows fade in one by one [fade up on every element]. A Form with Title, Notes, and a Date row that opens a second modal [every action a modal]. A full width Save in system blue [default blue tint]. The keyboard stays down until a tap on Title.

**The director's reasoning**:

1. The job is capture, not editing. flows.md, Reduce imposed effort: only the title and the date are needed now.
2. ios-components.md, Sheet row: a scoped task that returns to its parent. Medium detent, grabber, swipe to dismiss, Cancel leading, Add trailing.
3. ios-craft.md §4, the keyboard covers the field: focus the title on present.
4. ios-components.md, Text field row: offer choices over typing. Joi's quick add shows the shape: one title field, chips "Tomorrow" and "9:00 PM" above a full width Add, keyboard up. https://mobbin.com/screens/104de201-51d4-447d-9377-2ecf8d5d73a9. Mobbin returned no Things screen, so Things claims come from ios-craft.md §2.
5. ios-craft.md §2, put haptics on physical actions: one haptic on Add. ios-craft.md §6, ease out for enter and exit: one presentation, no per row fade.

**After**: Plus in the toolbar. A medium detent sheet rises with the keyboard. The title field is focused, placeholder "New To Do", style `.headline`. Under it, chips in `.subheadline`: Today, Tomorrow, and a calendar symbol that expands a compact date picker inline. No date by default. Cancel leading, Add trailing, disabled while the title is empty. Return commits. On Add the sheet dismisses, the row appears in Inbox with its date in secondary label color, and one success haptic plays.

**What a capture can and cannot verify**: A capture proves the sheet composition, chip order, and keyboard position. It cannot prove the haptic, the focus on present, or the dismiss gesture.

## 2. Live status: a flight screen plus a Live Activity

**Job**: A traveler at the gate wants to know whether the flight is on time without opening the app, and the full timeline when they do.

**Before**: Four stat tiles, Status, Gate, Delay, Weather [three or four stat tiles], each a card inside a card [cards inside cards], the on time tile with a green left bar [left accent bar]. A "Welcome back, Sam!" header [Welcome hero]. The Live Activity repeats the dashboard in miniature.

**The director's reasoning**:

1. research 10-design-director-methods.md §1, Dill: what must they achieve here. Two moments. The Island answers one question, the app the rest.
2. ios-craft.md §1: Flighty won for Live Activities modeled on airport boards, "one line per flight". Hypothesis: the line holds the next change the traveler can act on. ios-components.md names the Live Activities page with no rule text, so no HIG layout rule is cited.
3. evidence.md rule 2, open the image: Flighty's Detailed Timetable shows Scheduled and Estimated columns per step, green on time and red when late, in a sheet over a map. https://mobbin.com/screens/f642c78d-91ab-484f-b782-692aef2c174a. Retain the two numbers side by side. Tiles hide the sequence.
4. defaults-detector.md, stat tiles and cards inside cards: stats sit inside their section, as a grouped list with headers (ios-components.md, Lists vs grids row). ios-writing.md, AI copy tells: no greeting.
5. ios-components.md Part B, color roles: green and red carry status only. research 10 §6: not color alone, so a late value also gets a symbol.

**After**: Title "AA 6294", route and date as a subtitle. A grouped List with sections Depart and Arrive, one row per step, Scheduled and Estimated in `.body` with monospaced digits. Late values red with an exclamation symbol, on time green. Live Activity: the compact Island shows the airline symbol leading and "On time" or "+24m" trailing. Expanded: one line, "AA 6294, Gate B12, boards 5:30 PM", and a progress bar. The lock screen shows the same line, and a tap opens the timetable.

**What a capture can and cannot verify**: A capture proves the list, the colors, and the symbols. It cannot prove the Live Activity refresh, the Island content, or the push path. Test with the activity running.

## 3. Tray sequence: a three step confirmation in one sheet

**Job**: A person sending money picks a contact, enters an amount, and confirms, without losing the typed amount.

**Before**: Three sheets at the same large detent, each with a "Step 1 of 3" pill above the title [pill badge above the H1], a purple to blue header [LinearGradient purple blue], and a 300 ms ease in out [one global duration-300 ease-in-out]. Every button says "Continue". Each sheet dismisses before the next.

**The director's reasoning**:

1. ios-components.md, Sheet row: one sheet at a time, custom detents, grabber, swipe to dismiss, Done paired with Cancel or Back. So one sheet that changes height.
2. ios-craft.md §2, fly instead of teleport: Family trays have distinct heights per step, labels morph from Continue to Confirm, one piece of information per tray. Mobbin returned no Family screen. Stand in: Trust Wallet's Confirm send sheet lists From, To, Network, fee, Total above Continue, then a second "Processing..." sheet. https://mobbin.com/flows/3d09793e-60c8-4cdb-b70a-4bfe883f6b74. Retain the summary rows. Reject the second sheet.
3. ios-craft.md §6, use the platform spring: bounce 0 to 0.3, under 300 ms, ease out, one transition for the height change.
4. ios-writing.md rule 9: Continue used consistently, a closing verb at the end, here "Send $20". Hypothesis: the amount in the label cuts misreads. defaults-detector.md, pill and gradient rows: the heading leads, one solid accent.
5. ios-craft.md §6, let destructive actions wait for the gesture to end. ios-components.md, Progress row: an inline activity indicator in the button.

**After**: One sheet. Step one, a third of the screen: "Send to", a contact search field, recent contacts. Pick one and the sheet grows to half: the contact chip, an amount keypad, "Continue". Tap and it grows to a grouped summary, To, Amount, Fee, Total, and the label morphs to "Send $20". On release the button spins inline, then the sheet shrinks to one line, "Sent to Maya", with a checkmark and a success haptic. Done or a swipe closes it. Standard Back on later steps, Cancel on the first.

**What a capture can and cannot verify**: A capture per step proves the heights and labels. It cannot prove the morph, the spring, or what Back does to the typed amount.

## 4. Add transaction: amount, category, date, draft versus saved

**Job**: A person who paid cash for groceries logs $42.17 under Groceries today and wants to trust that it saved.

**Before**: A full screen Form with Title Case labels [Title Case everywhere]. Amount uses the default keyboard. Category opens a wheel. Then Date, Notes, Merchant. "Save Transaction" in system blue [default blue tint] under `.padding(13)` [random spacing]. After save a toast reads "Transaction saved!" [toast instead of in place status, ios-craft.md §4]. Swipe down discards everything.

**The director's reasoning**:

1. input.md, Ask for necessary work at an understandable moment: amount, category, date now. ios-components.md, Disclosure control row: the rest behind one disclosure.
2. ios-components.md, Text field row: match the keyboard type. Copilot's split transaction shows a numeric keypad, the amount in large type, category chips, and a SAVE bar above the keypad. https://mobbin.com/screens/ea307f13-0255-4b7d-a6ca-18db31407f9d. Retain the save bar at the keyboard edge. Copilot's blue gradient is a brand choice. evidence.md rule 8: diagnose, do not ban, do not copy.
3. ios-components.md, Picker row: a short list is a pull down button. Hypothesis: most people reuse a few categories, so recent ones show as chips. input.md, known defaults: Date is Today.
4. input.md, action to acknowledgment to outcome: draft is not saved. ios-components.md, Sheet row: confirm unsaved changes with an action sheet. ios-craft.md §2, Copilot keeps data local: sync is a separate status.
5. ios-writing.md, casing: one style per element type. Buttons title case, labels sentence case.

**After**: A medium detent sheet from the toolbar plus. The amount at the top in `.largeTitle`, rounded design, decimal pad up, placeholder "$0.00". Below it recent category chips and "All Categories", a searchable list in the sheet. A Date row reads "Today" with a compact picker. "More" reveals Notes and Merchant. Cancel leading, Save trailing, disabled at zero. Swipe down with edits opens an action sheet, "Discard Changes" then "Keep Editing". On Save the row appears at the top of today's group with a brief highlight and a success haptic. While sync is pending it shows a small cloud symbol.

**What a capture can and cannot verify**: A capture proves the field order, the keypad type, and the disabled Save. It cannot prove the draft survives a dismiss or the row survives a relaunch.

## 5. Empty state and first run, with the permission ask deferred

**Job**: A person opens a reading list app for the first time with nothing saved and should save one article before the app asks for anything.

**Before**: At launch an alert asks for notification permission. The list shows a "Welcome to Readlater!" hero with 40 pt padding [Welcome hero with big padding], a purple to blue card [LinearGradient purple blue], and a book emoji [emoji as icons]. No button. No loading or error state [missing empty, loading, and error states].

**The director's reasoning**:

1. ios-components.md, Empty state row, and ios-writing.md rule 10: guidance plus a button. Phantom's Watchlist shows the failure, "No items yet." and nothing to tap. https://mobbin.com/screens/20f19a13-03f6-4bf3-ad29-5eacda275faa. Noom's Grocery List puts an add field at the top, then "No items added yet" and one line of guidance. https://mobbin.com/screens/014fc596-8c4a-4b63-83ac-1f3ca18b9509. Retain the input at the top. Reject the exclamation mark.
2. ios-components.md, Alert row: never at launch. input.md, Ask for necessary work at an understandable moment. Ask at the first reminder. Hypothesis: it lands better after one saved item.
3. ios-components.md, Onboarding row: context specific tips over one flow.
4. defaults-detector.md, hero, gradient, three cards: a small header, then content. Missing states: design the highest consequence one first, here a failed fetch.
5. ios-writing.md rule 5: "Reading List", not "Your Reading List".

**After**: Large title "Reading List". One `.body` block: "Save an article from Safari with the Share button, or paste a link." One button, "Paste Link". A dismissible tip on the toolbar plus at first visit. No alert at launch. The first saved row shows the title, then the excerpt. When the person taps the bell on an article, one line says what the notification will hold, then the system dialog appears. If the fetch fails the row keeps the title and shows "Couldn't load. Tap to retry."

**What a capture can and cannot verify**: A capture proves the empty composition and the absence of a launch alert. It cannot prove the tip frequency or when the permission dialog fires.

## 6. Interruption and resume: a setup left mid way

**Job**: A person is on step three of a five step account setup, name, photo, bank link, limits, review, when a phone call arrives, and returns ten minutes later.

**Before**: Five full screen modals, each with a "Step 3 of 5" pill [pill badge], each over the last [every action a modal]. State lives in each screen's `@State`, so the relaunched app opens at step one, empty. Buttons are styled Text with `onTapGesture` [onTapGesture instead of Button].

**The director's reasoning**:

1. flows.md, Decisions to settle before implementation: what happens if the app is interrupted. input.md, Help people recover: no redoing unaffected work.
2. evidence.md rule 1: a capture proves composition only, so Mobbin was not searched for this case.
3. ios-components.md, Full screen modal row: a multistep task. One modal with a navigation stack and the standard Back. Progress row: a determinate bar. defaults-detector.md: real Buttons, text styles.
4. flows.md: do not invent backend capabilities. The draft is local. The bank link is a third party handoff, not a draft. Hypothesis: resuming on the first step with missing data beats resuming where the person left, because the link may have finished or failed meanwhile.
5. research 10 §6, Switch Control: no timeouts. The draft does not expire during the call.

**After**: One full screen modal, "Set Up Account", with a navigation stack, the standard Back, and a thin determinate progress bar under the title. Every field writes to a local draft on change. On return the modal reopens on the first step with missing data, steps one and two filled. If the bank link was in flight, step three shows an inline row, "Link not finished", with a "Continue Linking" button. The review step lists every value with a chevron, so a wrong photo is fixed without restarting. Cancel opens an action sheet, "Save Draft" and "Discard", Sheet row.

**What a capture can and cannot verify**: A capture proves the progress bar and the filled fields when staged. It cannot prove the draft survived a real suspension or the bank callback.

## 7. Error and retry: a save fails on the network

**Job**: A person saves a long journal entry on a train, the network drops, and they must not lose a word.

**Before**: Body text in `.gray` [grey body text]. On Save a modal spinner covers the screen [every action a modal]. On failure an alert titled "Error" reads "Oops! We couldn't save your entry. Please try again later!" with OK, the editor closes, and the text is gone [missing error state].

**The director's reasoning**:

1. input.md: preserve valid input when a request fails, and tell waiting from failure. ios-craft.md §2, Copilot keeps data local: save locally first, sync second.
2. ios-writing.md rule 12, never "Error". Rule 4, no "we". Rule 6, say how to fix, no "oops". Oura follows these: "Can't load chat. Wait a moment and try again." https://mobbin.com/screens/9dbf6e35-9643-449f-9d0f-c89cc6248a49. Bevel writes "We couldn't load this" under a Title Case heading. https://mobbin.com/screens/ce3d6d39-0356-43a0-be24-cd8bcf302c6f. All are load failures, so they show copy and placement only.
3. ios-craft.md §4, a toast instead of in place status. ios-components.md, Alert row: never purely informational. Perplexity shows the status inline with "Try again". https://mobbin.com/screens/53c1cd17-3832-45bf-adcc-d86bd15c7a15.
4. ios-components.md, Progress row: an inline activity indicator in the button. Status row: one warning haptic.
5. defaults-detector.md: body in label color, one symbol set.

**After**: Editor in `.body` label color. Save is the prominent toolbar action. On tap it spins inline and the text stays editable. On failure the entry is kept locally, the button returns to "Save", and a status row slides in under the toolbar: "Saved on this iPhone. Couldn't sync. Check the connection and tap Retry." with an inline Retry button, a warning symbol, and one warning haptic. On success the row reads "Synced" and fades on the next scroll. No alert, no toast. In the list the entry carries a cloud slash symbol until it syncs.

**What a capture can and cannot verify**: A capture proves the status row copy and placement. It cannot prove the text survived the failure or that Retry sent it. Use a deterministic failure fixture, input.md.

## 8. Undo and destructive action: delete from a list with no alert

**Job**: A person clearing Inbox swipes a task away and realises one second later it was the wrong one.

**Before**: Rows are cards with a red left bar when overdue [left accent bar] and a trash emoji button [emoji as icons]. Tap it and an alert asks "Are you sure you want to delete this item?" with Yes and No [every action a modal]. The row fades out over 300 ms [global duration-300]. No undo.

**The director's reasoning**:

1. ios-components.md, Alert row, and ios-writing.md rule 15: no alert for a common undoable delete. Rule 13: never Yes or No. Mobbin returned five alert deletes and no undo pattern: Joi "Do you want to delete this item?" https://mobbin.com/screens/232e633c-a229-47bd-9e95-53acc546fa99, Perplexity https://mobbin.com/screens/eb538ea7-fa47-4bc3-b534-bce460473e22, and Noom https://mobbin.com/screens/8039e2dc-7db3-4944-9ed1-9706c0bc5094. evidence.md rule 6: shipped alerts prove a convention, not that it is right. Noom clears a whole list, not undoable, where an alert fits.
2. ios-components.md, Swipe actions and Context menu rows: delete by swipe, the same action in the menu, destructive last and marked.
3. ios-components.md, Undo row: system gestures first, a button only when needed, named "Undo Delete". input.md: undo is not a promise unless the backend honors it, so the delete is soft. Hypothesis: an in place undo row is found more often than shake.
4. ios-craft.md §6, let destructive actions wait for the gesture to end: a full swipe commits on release.
5. defaults-detector.md: the bar becomes a red date label, the emoji becomes `trash.fill`, the fill variant for swipe actions, ios-components.md Part B.

**After**: A plain grouped List, overdue as a red date label with a symbol. A trailing swipe reveals Delete in red with `trash.fill`, and a full swipe commits on release. Long press opens a context menu, Delete last and marked destructive. The row collapses with the default spring and one rigid haptic. For a few seconds a bottom row reads "Deleted 'Call the dentist'" with an Undo button. Shake also undoes, as "Undo Delete". No alert. Deleting a whole project, rare and not undoable, gets an action sheet, Action sheet row.

**What a capture can and cannot verify**: A capture proves the swipe action, the symbol, and the undo row. It cannot prove shake undo, the undo window, or that the server kept the row.

## Limits

These are constructed cases. The real references are the Mobbin captures cited and the sources in the sibling files. No After design is shipped or user tested. Mobbin returned no Things or Family screen, and was not searched for case 6. Each Hypothesis stays a prediction until a person exercises it.
