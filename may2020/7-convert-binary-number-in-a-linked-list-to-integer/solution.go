/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func getDecimalValue(head *ListNode) int {
    result := 0
    for e := head; e != nil; e = e.Next {
 		result = result * 2 + e.Val
 	}
    return result
}

/*
 * from https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * Input: [1, 0, 1]
 * Output: 5
 * Expected: 5
 */
