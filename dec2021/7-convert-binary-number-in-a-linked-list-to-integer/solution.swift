/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func getDecimalValue(_ head: ListNode?) -> Int {
        var result = 0
        var node = head
        while (node != nil) {
            result = result * 2 + (node?.val ?? 0)
            node = node?.next
        }
        return result
    }
}

/*
 * from https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * Input: [1, 0, 1]
 * Output: 5
 * Expected: 5
 */
