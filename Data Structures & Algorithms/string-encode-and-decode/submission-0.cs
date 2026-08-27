public class Solution {

    public string Encode(IList<string> strs) {
        var sb = new StringBuilder();
        foreach (var s in strs) {
            sb.Append(s.Length).Append('#').Append(s);
        }
        return sb.ToString();
    }

    public List<string> Decode(string s) {
        List<string> result = new();
        int i = 0;
        while (i < s.Length) {
            int slash = s.IndexOf('#', i);
            int l = int.Parse(s.AsSpan(i, slash - i));
            i = slash + 1;
            result.Add(s.Substring(i, l));
            i += l;
        }
        return result;
   }
}
