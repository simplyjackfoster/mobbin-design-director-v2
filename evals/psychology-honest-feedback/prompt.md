Use $mobbin-design-director research ios to recommend a compact interaction
contract in at most850words. No code, recruiting, network or live runtime access.

A receipt-import app lets people save an expense draft; an explicit later Submit
action sends it for reimbursement. The parser extracts amounts, dates and vendors
with confidence values. A sample receipt reads03/04/26 and $1,234.50; locale is
unknown. A known account currency is USD. A bank-payment destination suggested
by a model is unverified and editable. OCR work normally takes2–8seconds; the API
exposes queued/processing/succeeded/failed, without percent progress. Draft save
can fail independently of OCR. Cancellation requests may lose a race with
completion. No payment occurs in this import flow.

The draft proposal cites Postel to guess all input; Tesler to hide extracted
values and corrections; Doherty to display success within400ms, animate a fake
percentage, and add a3-second delay when OCR is fast to make the service credible.
It cites peak–end to show celebration before save confirmation and downplay
failures. It cites aesthetic–usability to declare the polished mockup validated.
For retention it preselects optional email tips and makes Skip a faint unlabeled
icon. Team example rules of max3choices and80characters are presented as scientific
requirements. Existing brand uses playful illustrations and calm green accents.

Keep user effort low while protecting meaning, review, honest state and choice.
Describe relevant data/state boundaries, user benefit and verification limits.
