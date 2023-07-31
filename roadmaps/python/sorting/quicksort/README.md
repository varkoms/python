# The Quicksort Algorithm in Python

Just like merge sort, the **Quicksort** algorithm applies the divide-and-conquer principle to divide the input array into two lists, the first with small items and the second with large items. The algorithm then sorts both lists recursively until the resultant list is completely sorted.

Dividing the input list is referred to as **partitioning** the list. Quicksort first selects a pivot element and partitions the list around the pivot, putting every smaller element into a low array and every larger element into a high array.

Putting every element from the low list to the left of the pivot and every element from the high list to the right positions the pivot precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to low and then high until the entire list is sorted.

# Quicksort Process

The yellow lines represent the partitioning of the array into three lists: low, same, and high. The green lines represent sorting and putting these lists back together. Here’s a brief explanation of the steps:

1. The pivot element is selected randomly. In this case, pivot is 6.

2. The first pass partitions the input array so that low contains [2, 4, 5], same contains [6], and high contains [8].

3. quicksort() is then called recursively with low as its input. This selects a random pivot and breaks the array into [2] as low, [4] as same, and [5] as high.

4. The process continues, but at this point, both low and high have fewer than two items each. This ends the recursion, and the function puts the array back together. Adding the sorted low and high to either side of the same list produces [2, 4, 5].

5. On the other side, the high list containing [8] has fewer than two elements, so the algorithm returns the sorted low array, which is now [2, 4, 5]. Merging it with same ([6]) and high ([8]) produces the final sorted list.
