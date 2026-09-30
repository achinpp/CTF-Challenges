# RedCypher CTF — THE BETRAYAL (write-up / notes)

Flag format: `redcypher{...}` (case-insensitive)
Progress: **2 / 3 flags**

## Mission brief

> After the successful Five/Nine attack, fsociety begins rebuilding its remaining infrastructure. Without warning, the Dark Army strikes the surviving systems, exposing weaknesses and leaving traces behind. A forgotten relay operator may have documented the infrastructure before the attack.
>
> Lead: X username **@specter_2070**
> Trace the operator, follow the scattered records, and uncover the Dark Army's initial entry point.

---

## Flag 1 — The relay record

### 1. X / Twitter — @specter_2070 ("Evan Cross")
- Bio: `Infrastructure // Signal // R7`, joined Sep 2026, 4 posts.
- Profile/posts pulled via `https://api.fxtwitter.com/2/profile/specter_2070/statuses` (x.com blocks unauthenticated fetches).
- Posts:
  - "The relay was never meant to survive the migration... Search for the account that was **given a name before its owner chose one**." → Reddit's auto-generated usernames.
  - "The old discussion is still under the account: **Confident-Student-19**"
  - "The operation had a name before it had a route... `G _ O S T` — one character was removed." → **GHOST**
  - "Every record ended the same way: `signal / relay / return`"

### 2. Reddit — u/Confident-Student-19
- Read via RSS (`https://www.reddit.com/user/Confident-Student-19/.rss`) because the JSON API returned 403.
- Posts:
  - Archive is titled **"Cross Relay Notes"**, author Evan Cross. The useful entry is "the one that discusses the clock in the margin".
  - Record format: **`name / path / clock / node`**; path hint `R _ L A Y` → **RELAY**
  - "The profile connected to the archive uses an **email-based avatar service**" (→ Gravatar).

### 3. Blog — https://cross-relay-notes.blogspot.com
- Found by guessing hostnames. All posts dumped via `/feeds/posts/default?alt=json`.
- *The Name Before the Route*: `G _ O S T`, uppercase → NAME = **GHOST**
- *Old notes were written in a hurry*: margin number `0317` is the return-record ID → CLOCK = **0317**
- *The Dark Copy*: technical copy published under the name **`dark-specter`**, migration ID `R7-2069-MIGRATION`, "the final node was not R5" → NODE = **R7**
- *The Image That Stayed*: points to the email-based avatar (Gravatar) profile.
- Only comment: "Pastebin ???" (by Truth_Seeker, probably another player).

### 4. Pastebin — https://pastebin.com/u/dark-specter
- Paste **"R7 Migration Return Record"** (`https://pastebin.com/tFnDHqS5`):
  ```
  name: GHOST   path: RELAY   clock: 0317   node: R7
  The return channel requires the following phrase:
  GHOST//RETURN//0317
  The business identity is associated with the author profile.
  ```
- Note: GitHub user "Dark-Specter" is an unrelated real account (created 2024) — ignore.

### 5. Blogger profile → email
- https://www.blogger.com/profile/02712871808146672123
- Contact: **evancross6767@gmail.com**

### 6. Gravatar (lookup by SHA-256 / MD5 of the email)
- https://gravatar.com/chocolate1b5236239b — "Evan Cross", company **DArk**
- Mobile: **+94702943637**
- Avatar shows a "CROSSTECH SECURITY" monitor (unused so far).

### 7. WhatsApp — +94702943637
- WhatsApp Business account named **"Grant Chang"** (Dark Army leader in Mr. Robot).
- Sending `GHOST//RETURN//0317` → "[RETURN CHANNEL OPEN]... Continue through the verification channel: https://t.me/dArk_specterBot — Required format: `NAME-PATH-CLOCK-NODE`"

### 8. Telegram bot — @dArk_specterBot
- `/start` and `GHOST//RETURN//0317` → "Invalid relay key."
- **`GHOST-RELAY-0317-R7`** → "Access granted." + mission link (Google Drive) +

**FLAG 1: `RedCypher{GHO$T_RETURN_0317}`** ✅

---

## Flag 2 — The Phoenix station

### 1. Google Drive — "GeoTrace — Dark Army Relay.md"
- https://drive.google.com/file/d/1KDiQdZzAuCt4KHuQj7VUiiSkAjLNQ2By/view
- Mission `DA-PHX-07`. Fragments:
  ```
  REGION: PHOENIX
  ROAD_REFERENCE: CENTRAL
  SECONDARY_REFERENCE: INDIAN SCHOOL
  NETWORK: URBAN TRANSPORT
  ```
- "The location has not disappeared. Someone left a trace behind." → a Google Maps review.
- File content downloaded raw — no hidden text.
- The Drive "owner" field shows a personal email that appears to belong to a real person (probably the CTF author). **Not pursued**, since it's outside the challenge.

### 2. Location
- Valley Metro Rail (B Line) — **Indian School/Central Ave** light rail station, Phoenix, AZ 85012 (aka Steele Indian School Park station).
- Google Maps: **Stop ID 10006**, plus code FWWG+8F.

### 3. Google Maps review (the "trace")
- Posted by **"Shadow Sovereign"** (Local Guide Level 2), contributor ID `106751395138011084052`:
  > If you're trying to identify the exact station, check the map carefully — the station name and reference number are both listed there.
  > `RedCypher{station-name_Station-code}`
- Flag built from station name + stop ID `10006` (e.g. `RedCypher{Indian-School-Central-Ave_10006}`).

**FLAG 2:** ✅ accepted (station name + `10006`)

Feedback after flag 2:
> They're collecting information outside their clearance. The real question isn't what they have—it's who they're going to betray.

---

## Flag 3 — In progress

### Checked, no result
- The Shadow Sovereign Maps account has only 1 review and 0 photos/edits (checked via the Maps contributor API). Its avatar is a generic hooded-hacker image with no hidden data.
- Other "Shadow Sovereign" / "ShadowSovereign" accounts (X, Pastebin, Blogspot, Gravatar, Reddit) are old and unrelated.
- The Reddit account has no comments. The blog has no hidden pages or hidden HTML text.
- dark-specter's Pastebin has only the one paste.
- The images (X cat avatar, Blogger portrait, Gravatar avatar and header) have no embedded strings or appended data.

### Next steps to try
1. Telegram bot: send the accepted flag-2 answer, `10006`, `/next`, `/help`. It gave mission 2 after flag 1, so it may give mission 3 after flag 2.
2. TRANSMIT page: check for a new mission card or text under the "2 / 3" feedback.
3. WhatsApp "Grant Chang": send the flag-2 answer and see whether there's a new auto-reply.
4. Unused leftovers: `CROSSTECH SECURITY` (Gravatar avatar), `R7-2069-MIGRATION`, R5-RELAY → R7-BROADCAST, company "DArk".

---

## Tools and tricks used
- `api.fxtwitter.com` to read X profiles and posts without logging in.
- Reddit `.rss` feeds when the JSON API is blocked.
- Blogger `/feeds/posts/default?alt=json` and `/feeds/comments/default?alt=json` to dump posts and comments.
- Gravatar lookup by email hash: `api.gravatar.com/v3/profiles/<sha256(email)>` and `gravatar.com/<md5(email)>.json`.
- `api.whatsapp.com/send/?phone=<number>` shows the business name.
- Google Maps contributor data via the `locationhistory/preview/mas` endpoint.
- Drive `uc?export=download&id=<id>` to get raw file content.
