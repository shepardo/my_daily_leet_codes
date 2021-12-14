

/*
(Premium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

The following property amazingly holds:
Let T tree be a binary tree.
Let T.R be a root in a binary tree.
Let A, B be nodes in T
Let L be the lowest common ancestor of A, B in T
Let P(c, d) be a function calculating the path length between any nodes c, d in T
P(A, T.R) + P(B, L) = P(B, T.R) + P(A, L)

Once you prove that if P(A, T.R) = P(B, T.R), then P(A, L) = P(B, L),
then the total proof follows cleanly from there due to the equality
property of addition.

This property enables the composition of following algorithm to solve the LCA problem.
There are clearly other ways to solve this problem, but I find this solution very satisfying.
*/

class Solution {
public:
    Node *lowestCommonAncestor(Node *A, Node *B) {
        Node *a = A;
        Node *b = B;

        while (a != b) {
            a = ( a == nullptr ) ? B : a->parent;
            b = ( b == nullptr ) ? A : b->parent;
        }
        return a;
    }
}


