/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int result = 0;
        ListNode *node = head;
        while (node != nullptr) {
            result *= 2;
            result += node->val;
            node = node->next;
        }
        return result;
    }
};


/*
 * from https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * Input: [1, 0, 1]
 * Output: 5
 * Expected: 5
 */
