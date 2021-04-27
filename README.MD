Name: Mena Bebawy
Date: April 26, 2021

Methodology:

1. I started by deciding on which language to use. Python is not my native language, however, it seemed like the suitable language to use given its graphing library.
2. I started by thinking about computing the averages using the brute force method.
   However, I decided that a better method could be used that would be much faster.
   I would iterate through the list, drop the last value, and add the next one, giving us an
   O(n) worst case.
3. The space complexity is also O(n-m) where n is the number of input values and m is the length of the
   rolling average.
4. I plotted the rolling averages and it produced a reasonable result that aligned with the given example.
5. I computed the max value using a simple loop.
6. I thought of possible edge cases that could apply in this program.

---

To run:
python rolling_averages.py

---
Result:
Result is stored in result.png
