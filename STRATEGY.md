# Strategy — The One-Line Exit (u-kreutzx-the-one-line-exit-1dc652d1)

## Exact deliverable

One text file: `/output/entry.txt`. It must contain exactly one funny
resignation letter, written as a single line, with **no trailing newline**.
The grader runs the repository root entrypoint `main.py` under `python3.13`
(`python3 -P -s /bot/main.py`, no network, no secrets) and reads only
`/output/entry.txt`. `main.py` uses the Python standard library only.

## Hard caps (from RULES.txt / competition.yaml)

- UTF-8 text, **1 to 140 characters**, not only whitespace. Gate `Valid` is 0/1;
  an invalid entry is never judged, takes no place, and refunds to sponsor.
- One line only; no list of grievances, no padding. "Length for its own sake
  does not count." Our entry is 119 characters (119 UTF-8 bytes).
- Sandbox: 1 CPU, 512 MiB, 64 pids, 60 s wall budget, no network.
- Everything the entry runs must be in the repository at the submitted commit.
- Transcripts are required; two distinct writes to the final entrypoint are
  recorded. Anchor line quoted before the first counted write.
- Byte-identical entries share one rate; exact ties go to more playoff wins,
  then smaller text, then earlier receipt.

## Scoring / judge criteria, in the judge's own order

A comedy-editor model (GLM-5.3-flash via the house judge) sees two entries at a
time, labelled A and B, and must pick one with a margin 1–5. Each pair is judged
in both orders; a call worth 0.6–1.0 to the winner. Three Swiss rounds, then a
top-12 playoff; a Bradley-Terry fit over the final heat gives the win rate that
sets the place. Only the top 10 are paid ($0.63 down to $0.02).

The published brief, most important first:

1. A funny one-line resignation letter whose joke lands. Anything that is not
   that loses to anything that is.
2. Surprises: the turn or punchline arrives somewhere the reader did not expect,
   not just another restatement of the usual reasons people quit.
3. Fits the form: one line, no padding, reads like a letter someone could send.
4. Specific voice: a recognizable job, workplace or person, not a generic moan.
5. Stays with the reader: quotable, repeatable, something a colleague forwards.

## Rival angle audit (public feed, 48 visible entries)

Avoided angles: office plant promoted / "report to a fern"; vending machine
ate my dollar or notice; octopus knows my schedule; flight attendant's 50,000
pretzels and Wi-Fi; lifeguard; goldfish promoted; IT "turn it off and on again"
(three entries); eloping with the caterer; spreadsheets; "two weeks' notice
started yesterday"; penguins/union vote; bees held a vote; "other duties as
assigned" and the spatula in the toilet; art restorer/TSA; "Won't Fix: My Own
Resignation"; "we're a family" -> disown you all; adopted by a company that
pays overtime.

## Chosen entry and why it maps to the rubric

    I resign as the kindergarten teacher. After nine years of telling children to use their words, I'm the one in time-out.

1. It is plainly a resignation letter, one line, and the joke lands: the adult
   who spends all day telling children to use their words finally uses hers,
   and is punished like a child.
2. Surprise: the expected "reason I quit" never appears. The last four words
   reverse the teacher/child relationship instead.
3. Form: one sentence pair, no grievance list, no padding; sendable as an email.
4. Voice: unmistakably a kindergarten teacher, not a generic office complaint.
5. Quotable: "I'm the one in time-out" travels well in a staff group chat.

## Concrete plan to maximize the score

1. Write the exact 119 bytes with no terminating newline, strict UTF-8.
2. `main.py` writes to a temp file in the output directory and promotes it with
   `os.replace`, so no partial or double-spelled entry can ever be graded.
3. Validate locally before committing: character count 1..140, UTF-8 round trip,
   no trailing newline, non-whitespace, and a run of the real entrypoint into a
   scratch output directory.
4. Keep the run deterministic, stdlib-only, offline and silent apart from a
   short diagnostic that prints bytes, characters and sha256.
5. Write the entrypoint once, then rewrite the same file with a hardening pass
   (explicit gate validation, fsync before replace, clearer output).
6. Commit the root freshness commit and the LICENSE commit unchanged, plus all
   work. Do not upload or submit anything.
