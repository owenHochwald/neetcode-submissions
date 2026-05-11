class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> lookup = new HashMap<>();

        s.chars().forEach(c -> lookup.put((char) c, lookup.getOrDefault((char)c, 0) + 1));
        t.chars().forEach(c -> lookup.put((char) c, lookup.getOrDefault((char)c, 0) - 1));

        return lookup.values()
            .stream()
            .allMatch(v -> v == 0);



    }
}
