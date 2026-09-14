KERNEL ECHO
Story Part: 1. Recruitment
Difficulty: Red Hat Hacker
Category: Reverse Engineering + Cryptography
Author/Owner: Vidasun / Janidu

Black Lantern runs an encrypted courier network for its criminal operations.
Intelligence officers captured relay-07 and recovered a traffic spool, its log,
and a compiled fragment of the courier software. The original source is gone.

The organization trusts its encryption. Its rushed deployment may tell another
story: clock records and repeated relay state survived the seizure.

One courier message is believed to identify a secret midnight exchange. As the
analyst being recruited for this operation, recover the location and submit
the authentic message's authentication token before the exchange occurs.
The exchange time is part of the fictional story; this package never expires.

FILES
README.txt                  This briefing.
relay.log                   Recovered relay operations journal (UTC).
intercepted_messages.json   Captured traffic with approximate relay metadata.
courier_core.pyc            Recovered CPython 3.14.4 bytecode (cpython-314).
SHA256SUMS.txt              Integrity hashes of the four other player files.

OBJECTIVE
Recover the authentic courier message and submit its complete token.
Flag format: REDCYPHER{...} (case-sensitive).

False signals and diagnostic bait may exist. A printable token is not proof
that it came from authentic courier traffic.

The bytecode is version-specific. Use the matching CPython minor version for
standard-library disassembly; third-party decompiler support may vary.
No network access, live target, or executable service is required to play.
