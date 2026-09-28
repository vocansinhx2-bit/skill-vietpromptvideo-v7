<REFERENCE MAP if needed>
<GLOBAL INVARIANTS>
<INITIAL STATE>
<SEQUENCE / SHOTS / TIMELINE at model-appropriate granularity>
<CAMERA / PERFORMANCE if needed>
<AUDIO if needed>
<CONTINUITY / FINAL STATE>

Rule: omit empty branches and all design-time commentary.

## Seedance 2.5 block order
FORMAT: <duration>s, <aspect ratio>, <style one line>.
REFERENCE ROLES: @Image1 = <one narrow role>. Do not copy <leak-prone attribute> from @Image1. (repeat per asset, numbered in upload order)
SUMMARY: <one sentence: who, where, what changes>.
STARTING STATE: <positions, props, screen side, light>.
TIMELINE:
0-<t1> seconds: <cause -> action -> visible result>. Ends with <state>.
<t1>-<t2> seconds: <continues from previous end state>. Ends with <state>.
CAMERA: <one main intention per segment, speed, framing>.
LIGHTING: <direction, hard/soft, contrast, base/secondary/accent color>.
AUDIO: (music) <sfx> {Speaker, language: "line"} 【subtitle】 or "No background music" / "No subtitles".
ENDING STATE: <final positions, props, expression>.
CONSTRAINTS: <identity lock, no extra people, no text, no replay>.

Rules: segments contiguous and non-overlapping; each action described once; one speaker per lip-sync shot; last-frame continuation uses "Use @Image1 as the exact first frame and continue forward. Do not replay the previous action."
