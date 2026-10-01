# Advanced Algorithms — Project 1 (CPSC 535, Fall 2024)

Algorithm design problems solved for CSUF's CPSC 535 Advanced Algorithms, each with a baseline and an improved solution.

**Team:** Parastoo Toosi, Deepthimayi Pesala, Roszhan Raj Meenakshi Sundhresan

| File | Problem | Approach |
|---|---|---|
| `q1_pair_sum_and_join.py` | **Task A — Shipping two items:** find two products whose prices sum to $2500, or `NIL`. **Task B — Database join:** join two keyed lists `L(k, x)` and `R(k, s)` into `(k, x, s)`. | Baselines are O(n²) nested loops; improved versions sort and use two pointers in O(n log n). |
| `longest_string_chain.py` | Longest chain of words where each word is formed by adding one letter to the previous one. | Sort by length, then dynamic programming over "remove one character" predecessors. |
| `q3_unique_starting_city.py` | Cities on a circular road, each with a gas station: find the one city where a car with an empty tank can start, loop all the way round and return without running out of fuel. | Single greedy pass tracking total and current fuel balance, O(n). |

## Run

```sh
python3 q1_pair_sum_and_join.py
python3 longest_string_chain.py
python3 q3_unique_starting_city.py
```
