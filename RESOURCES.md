# 📚 Resources

Curated, not exhaustive — every entry here is something genuinely useful for the patterns this repo covers, organized so it's easy to add to without becoming a link dump.

---

## Books

| Title | Why it's here |
|---|---|
| *Grokking Algorithms* — Aditya Bhargava | Closest thing to this repo's own style: intuition-first, visual, beginner-friendly. Good companion for the Foundations/Arrays phase. |
| *Cracking the Coding Interview* — Gayle Laakmann McDowell | Standard interview-prep reference once more patterns (trees, graphs, DP) are covered. |
| *Introduction to Algorithms (CLRS)* — Cormen, Leiserson, Rivest, Stein | The rigorous reference for when "why does this work" needs a formal proof, e.g. why Euclidean GCD is O(log(min(a,b))). |

## Courses & Videos

| Resource | Best for |
|---|---|
| NeetCode (neetcode.io) | Pattern-based problem sets that map closely to `PATTERNS.md` in this repo — Two Pointers, Binary Search, etc. are organized the same way. |
| Abdul Bari (YouTube) | Strong visual explanations of sorting algorithms (bubble/selection/insertion/merge/quick) — good pairing for `SORTING ALGORITHMS/` and `QUICK SORT/`. |
| MIT 6.006 (OpenCourseWare) | Once Trees/Graphs/DP start — more rigorous than most YouTube content. |

## Articles / Pattern References

| Resource | Best for |
|---|---|
| "14 Patterns to Ace Any Coding Interview" (educative.io / various mirrors) | The original framing behind organizing problems by pattern rather than topic — this repo's `PATTERNS.md` follows the same idea. |
| GeeksforGeeks — Block Swap Algorithm | Referenced directly in `Array/left_rotation.py`'s block-swap rotation approach. |
| GeeksforGeeks — Euclidean Algorithm | Background for the three GCD approaches in `RECURSION - 3/gcd.py`. |

## Visualization Tools

| Tool | Use case |
|---|---|
| VisuAlgo (visualgo.net) | Step-through visualizations for sorting, binary search, and (later) trees/graphs. |
| Python Tutor (pythontutor.com) | Line-by-line execution + call stack visualization — especially useful for debugging recursion (`RECURSION/` through `RECURSION - 4/`). |

## Practice Platforms

| Platform | Notes |
|---|---|
| LeetCode | Primary platform this repo tracks against — problem numbers are cross-referenced in `PATTERNS.md` and `MASTER_TABLE.md`. |
| NeetCode 150 / Blind 75 | Curated problem lists that align well with the pattern coverage gaps noted in `PATTERNS.md` (Sliding Window, Backtracking, Trees, Graphs, DP). |

## Complexity References

| Resource | Use case |
|---|---|
| Big-O Cheat Sheet (bigocheatsheet.com) | Quick lookup table — same content as the complexity tables in `INTERVIEW_REVISION.md`, more exhaustive. |
| Python Wiki — Time Complexity (wiki.python.org/moin/TimeComplexity) | Authoritative source for built-in list/dict/set operation complexities referenced throughout the per-folder READMEs. |

## Useful GitHub Repositories

| Repo | Why |
|---|---|
| `azl397985856/leetcode-js-leetcode` and similar pattern-tagged solution repos | Cross-reference for alternate solutions once a problem here is solved, to compare approaches. |
| Any actively maintained "awesome-leetcode-resources" list | Good for discovering company-specific problem sets once interview prep gets targeted. |

---

*Add to this file as new resources prove useful — don't remove old ones unless they're outdated, since "what helped at each stage" is itself useful history.*
