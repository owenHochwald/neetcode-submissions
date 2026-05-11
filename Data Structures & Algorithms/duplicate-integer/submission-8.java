class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> lookup = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            if (lookup.contains(curr)) {
                return true;
            }
            lookup.add(curr);
        }
        return false;
        
    }
}