//hash Map import 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer,Integer>();
        int complement = 0;
        int[] arr = {0,0}; 
        for(int i = 0; i < nums.length; i++){
            complement = target - nums[i];
            if (seen.containsKey(complement)){
                arr[0] = seen.get(complement);
                arr[1] = i;
                return arr;
            }
            seen.put(nums[i],i);
        }
        return arr;
    }

}
