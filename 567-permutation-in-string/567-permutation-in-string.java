class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int l1 = s1.length(), l2 = s2.length();
        if (l1 > l2) {
            return false;
        }
        HashMap<Character, Integer> needs = new HashMap<Character, Integer>();
        HashMap<Character, Integer> window = new HashMap<Character, Integer>();
        for (int i = 0; i < l1; i++) {
            char c = s1.charAt(i);
            int count = needs.getOrDefault(c, 0);
            needs.put(c, count + 1);
        }
        int left = 0, right = 0;
        int valid = 0;
        while (right < l2) {
            char c = s2.charAt(right);
            right++;
            if (needs.containsKey(c)) {
                int count = window.getOrDefault(c, 0);
                window.put(c, count + 1);
                if (window.get(c).intValue() == needs.get(c).intValue()) {
                    valid++;
                }
            }
            while (valid == needs.size()) {
                if (right - left == l1) {
                    return true;
                }
                char d = s2.charAt(left);
                left++;
                if (needs.containsKey(d)) {
                    if (window.get(d).intValue() == needs.get(d).intValue()) {
                        valid--;
                    }
                    window.put(d, window.get(d) - 1);
                }
            }
            
        }
        return false;
    }
}