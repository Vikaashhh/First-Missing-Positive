# Day 13 of #gfg160 - Maximum Circular Subarray Sum

## 🧠 Problem:
Given an array of integers, the goal is to find the maximum possible sum of a subarray, where the subarray can be circular (i.e., wrap around the end of the array to the beginning).

## 🔍 Key Insight:
There are two possibilities:

1. Non-Circular Case – Use Kadane’s Algorithm to get the max subarray sum normally.

2. Circular Case – The max circular subarray sum is: Total Sum of Array - Minimum Subarray Sum
✅ This effectively includes the wraparound portion by excluding the minimum subarray.

---
## ⚠️ Edge Case:
If all elements are negative, the circular sum becomes zero — which is invalid. So, return the non-circular max in such cases.

---
## 🔖 Hashtags:
#Day13 #gfg160 #geekstreak2025 #dsa #python #codingchallenge #100DaysOfCode #datastructures #kadanesalgorithm #leetcode #codingjourney #devcommunity #circulararray #vscode #cleanCode #linkedintips

## ✍️ Author
Crafted with clarity by Vikash Joshi 
