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
    public List<Integer> inorderTraversal(TreeNode root) {
       List inorderList = new ArrayList<Integer>();
       return search(root,inorderList);
    }
    public List<Integer> search(TreeNode root, List<Integer> list){
        if (root == null){
            return list;
        }
        search(root.left,list);
        list.add(root.val);
        search(root.right,list);
        return list;

    }
}
