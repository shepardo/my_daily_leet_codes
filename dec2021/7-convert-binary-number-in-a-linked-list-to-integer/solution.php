/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @return Integer
     */
    function getDecimalValue($head) {
        $result = 0;
        while (!is_null($head)) {
            $result = $result * 2 + $head->val;
            $head = $head->next;
        }
        return $result;
    }
}

/*
 * from https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * Input: [1, 0, 1]
 * Output: 5
 * Expected: 5
 */
