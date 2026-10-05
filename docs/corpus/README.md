# Current Corpus Work

`PROTOCOL.md` defines the current corpus stress-test methodology. After checkpoint 124, the next active corpus phase is a **multi-book stress pass** using canonical surface v0.8 to look for remaining semantic, discourse, vocabulary, and world-interface gaps before beginner/glyph work.

Completed prose-pass reports are historical evidence and now live under `archive/corpus/`. Current translation-regression truth is executable under `tests/`, especially the corpus bridge, gap-completion, post-minimization, stabilization, cross-genre, and Yona vocabulary tests.

When new corpus pressure changes the language:

1. update the relevant current spec/data;
2. add an executable regression;
3. summarize the current result in `docs/CURRENT_STATE.md`;
4. archive the completed prose pass rather than leaving generations of pass reports mixed with current documentation.
