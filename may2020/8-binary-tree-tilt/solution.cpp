/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 class Solution {
 private:
     int tilt_acc;
 public:
     int findTilt(TreeNode* root) {
         this->tilt_acc = 0;
         if (root == nullptr)
             return 0;
         int left_tilt = (root->left != nullptr)? this->doFindTilt(root->left) : 0;
         int right_tilt = (root->right != nullptr)? this->doFindTilt(root->right) : 0;
         this->tilt_acc += abs(right_tilt - left_tilt);
         return this->tilt_acc;
     }

     int doFindTilt(TreeNode* node) {
         if (node == nullptr) {
             return 0;
         } else {
             if (node->left == nullptr && node->right == nullptr) {
                 return node->val;
             } else {
                 int tuple_left = (node->left != nullptr)? this->doFindTilt(node->left) : 0;
                 int tuple_right = (node->right != nullptr)? this->doFindTilt(node->right) : 0;
                 this->tilt_acc += abs(tuple_left - tuple_right);
                 return tuple_left + tuple_right + node->val;
             }
         }
     }
 };
