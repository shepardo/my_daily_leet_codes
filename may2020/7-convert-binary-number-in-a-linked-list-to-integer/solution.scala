/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def getDecimalValue(head: ListNode): Int = {
        def doGetDecimalValue(result: Int, head: ListNode): Int = {
          if (head == null) result else doGetDecimalValue(result * 2 + head.x, head.next)
        }
        doGetDecimalValue(0, head)         
        //if (head == null) 0 else (head.x * 2) + getDecimalValue(head.next)
    }
}

/*
 * from https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * Input: [1, 0, 1]
 * Output: 5
 * Expected: 5
 */
