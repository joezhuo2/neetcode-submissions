public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> map = new();
        foreach (var s in strs) {
            char[] count = new char[26];
            foreach (char c in s) {
                count[c - 'a']++;
            }

            string key = new string(count);

            if (!map.TryGetValue(key, out var list)) {
                list = new();
                map[key] = list;
            }

            list.Add(s);
        }
        return new List<List<string>>(map.Values);
    }
}
