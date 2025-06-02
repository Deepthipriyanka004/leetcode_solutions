// Last updated: 6/2/2025, 6:36:01 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum=0;
    public TreeNode bstToGst(TreeNode root) {
        transverse(root);
        return root;
    }
    public void transverse(TreeNode root){
        if(root==null){
            return;
        }
        transverse(root.right);
        sum+= root.val;
        root.val=sum;
        transverse(root.left);
    }
        
    
}