# Committed-snapshot verification after pass 19

22 September 2026. Research was committed locally as
fda4bab3d552a49bcd059730e55dc706f2d2e461. A fresh archive of that commit
passed all nine suites and reproduced all eight analytical reports. Its PDF
rebuilt with the same text and size but a different path-dependent trailer ID.
This was an artifact reproducibility defect, not a mathematical test failure.

The PDF builder was corrected by omitting pdfTeX's optional path-dependent
trailer identifier, while retaining the fixed metadata date. The correction
was committed as 56487a4ec63e3a0541ee30b2da30939678307d8c, tree
45d96945fe33baf0abba77c8aae2180115cb4bec. A fresh archive of that exact commit
again passed all nine suites, reproduced all eight reports byte for byte,
and rebuilt the committed PDF byte for byte. The original LICENSE and both
historical checkpoint trees equal the session's starting main.

The final PDF has 20 pages and 407,474 bytes. Its SHA-256 is
5f6965ed0f35e49a00306d3577bd51f004d65a7aabcb38d8660aca4154e52d17.
All 20 rendered pages were visually inspected before the metadata correction;
all 20 corrected renderings were then compared pixel for pixel with those
inspected pages and were identical. The corrected PDF's extracted text is
also identical. The build has no unresolved references or overfull boxes.

[The machine-readable execution record](../results/pass19-committed-verification.json)
contains the actual tested local commit/tree and report hashes. These commit
identifiers are local provenance anchors, not instructions to reset a later
remote branch. A recording commit adds this note, the execution record and
navigation only. The final publication procedure also verifies that recording
commit from its archive, reconciles current remote main, and checks the remote
ref/tree after a non-forced push. If connector-based publication creates a
commit with different metadata, equality of its full content tree with the
tested final local tree is required; do not claim commit-ID equality.

The analytical claims still rest on the written proofs, and the source-
comparison and service-meaning questions remain open. Restart instructions
are in continuation-pass18-19.md and work_orders/CURRENT.md; pass 20 has only
completed its exact algebraic opening, not the primary-source comparison.
