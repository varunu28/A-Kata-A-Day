// Find Max Tree Node
// Level 7Kyu
/*
 * You are given a binary tree. Implement the method findMax which returns the maximal node valuein the tree.
 */

public class FindMaxValueInTree {

    static int findMax(TreeNode  root) {
        if (root == null) {
            return Integer.MIN_VALUE;
        }
        
        return Math.max(root.value, Math.max(findMax(root.left), findMax(root.right)));
    }
}

