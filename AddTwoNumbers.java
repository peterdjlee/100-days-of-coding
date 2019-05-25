// You are given two non-empty linked lists representing two non-negative integers. 
// The digits are stored in reverse order and each of their nodes contain a single digit. 
// Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
    }
}

// THOUGHTS
Solution 1:
    If the number of digits are the same, add the corresponding digits:
        Case 1: sum < 10 => create a new node with the sum create the next node
        Case 2: sum >= 10 => create a new node with sum%10 create the next node with val + 1
    Pseudocode:
        sumNode = new ListNode(0)
        while l1 != null and l2 != null
            sum = l1.val + l2.val
            if sum < 10
                sumNode = new ListNode(sum)
                sumNode = sumNode.next // sets sumNode to null
            if sum >= 10
                sumNode = new ListNode(sum % 10)
                l1.next.val++ // add one to the next digit
                sumNode = sumNode.next
            l1 = l1.next
            l2 = l2.next
            

            