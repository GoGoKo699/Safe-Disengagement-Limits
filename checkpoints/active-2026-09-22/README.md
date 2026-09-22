# S1 — Active readiness checkpoint

**22 September 2026.** A candidate theorem about the ongoing resource cost of
remaining able to remove a cooperative controller within a deadline. Publication
novelty and a concrete engineering instantiation are not yet established.

Start with **NOTE.md**, sections 1-6. The two principal results are:

- Exact worst-case exit time from k ready modules and n-k cold modules.
- Exact normal-performance/exit-readiness frontier against all admissible
  preparation histories, including partial and rotating preparations.

Section 8 contains an assumption-changing countermodel: proportional preparation
invalidation removes the staircase and gives a continuous frontier. Do not omit
that qualification when describing the result.

Read **LITERATURE.md** for primary-source comparisons and claims already covered
by live-migration research. This is not a new protocol for VM migration and is
not a general AI-shutdown theorem.

Run the finite checks locally with Python 3.10+:

```sh
python verify.py
```

No cloud resources or third-party dependencies are needed. The program writes
**RESULTS.json**. It checks finite algebraic identities and local proof
certificates; it does not enumerate all continuous schedules or provide empirical
validation. **SHA256SUMS.txt** records the files in this checkpoint, excluding
itself and the outer zip.

The preceding passive-commitment checkpoint is deliberately not overwritten.
There is no S1 GitHub repository associated with this archive at creation time.
