class Solution {
    public boolean find132pattern(int[] nums) {
        if (nums.length < 3) {
            return false;
        }
        int[] left_min = new int[nums.length];
        Stack <Integer> stack = new Stack < > ();
        left_min[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            left_min[i] = Math.min(left_min[i-1], nums[i]);
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            if (stack.size() > 0 && nums[i] > stack.peek()) {
                while (stack.size() > 0 && nums[i] > stack.peek()) {
                    int n = stack.pop();
                    if (n > left_min[i]) {
                        return true;
                    }
                }
            }
            stack.push(nums[i]);
        }
        return false;
    }
}