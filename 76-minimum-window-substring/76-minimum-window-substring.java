class Solution {
    public String minWindow(String s, String t) {
        int m = s.length(), n = t.length();
        if (m < n) {
            return "";
        }
        int left = 0, right = 0;
        int start = 0, l = Integer.MAX_VALUE;
        HashMap<Character, Integer> needs = new HashMap<Character, Integer>();
        for (int i = 0; i < n; i++) {
            char c = t.charAt(i);
            int count = needs.getOrDefault(c, 0);
            needs.put(c, count + 1);
        }
        HashMap<Character, Integer> window = new HashMap<Character, Integer>();
        int valid = 0;
        while (right < m) {
            char c = s.charAt(right);
            right++;
            if (needs.containsKey(c)) {
                int count = window.getOrDefault(c, 0);
                window.put(c, count + 1);
                if (window.get(c).intValue() == needs.get(c).intValue()) {
                    valid++;
                }
            }
            //System.out.printf("%s, %s\n", start, l);
            while (valid == needs.size()) {
                if (right - left < l) {
                    start = left;
                    l = right - left;
                }
                char d = s.charAt(left);
                left++;
                if (needs.containsKey(d)) {
                    if (needs.get(d).intValue() == window.get(d).intValue()) {
                        valid -= 1;
                    }
                    window.put(d, window.get(d) - 1);
                }
            }
        }
        return l == Integer.MAX_VALUE ? "" : s.substring(start, start + l);
    }
}