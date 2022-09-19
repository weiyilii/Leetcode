class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int l1 = s.length(), l2 = p.length();
        if (l1 < l2) {
            return new ArrayList();
        }
        HashMap<Character, Integer> needs = new HashMap();
        for (int i = 0; i < l2; i++) {
            char c = p.charAt(i);
            int count = needs.getOrDefault(c, 0);
            needs.put(c, count + 1);
        }
        HashMap<Character, Integer> window = new HashMap();
        int left = 0, right = 0, valid = 0;
        List<Integer> res = new ArrayList();
        while (right < l1) {
            char c = s.charAt(right);
            right++;
            if (needs.containsKey(c)) {
                int count = window.getOrDefault(c, 0);
                window.put(c, count + 1);
                if (window.get(c).intValue() == needs.get(c).intValue()) {
                    valid++;
                }
            }
            while (valid == needs.size()) {
                if (right - left == l2) {
                    res.add(left);
                }
                char d = s.charAt(left);
                left++;
                if (needs.containsKey(d)) {
                    if (window.get(d).intValue() == needs.get(d).intValue()) {
                        valid--;
                    }
                    window.put(d, window.get(d) - 1);
                }
            }
        }
        return res;
    }
}