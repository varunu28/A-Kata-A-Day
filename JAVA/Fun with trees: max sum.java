// Fun with trees: max sum
// Level: 6kyu
/*
 * You are given a binary tree. Implement the method maxSum which returns the maximal sum of a route from root to leaf. 
 */

class Solution {
    static int maxSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        return root.value + Math.max(maxSum(root.left), maxSum(root.right));
    }
}
