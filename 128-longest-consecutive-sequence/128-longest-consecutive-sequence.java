class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 0;
        Set<Integer> num_set = new HashSet<Integer>();
        for (int num: nums) {
            num_set.add(num);
        }
        for (int num: num_set) {
            if (!num_set.contains(num-1)) {
                int cur_len = 1;
                int cur_num = num;
                while (num_set.contains(cur_num + 1)) {
                    cur_len++;
                    cur_num++;
                }
                res = Math.max(res, cur_len);
            }
        }
        return res;
    }
}