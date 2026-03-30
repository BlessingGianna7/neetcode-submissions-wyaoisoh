class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() == t.length()){
            char[] n = s.toCharArray();
            Arrays.sort(n);
            String sortedN= new String(n);
            char[] m = t.toCharArray();
            Arrays.sort(m);
            String sortedM= new String(m);

            return sortedN.equals(sortedM);
        }
        return false;
}
}
