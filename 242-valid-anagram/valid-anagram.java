class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        char[] char1= new char[s.length()];
        char[] char2= new char[t.length()];
        for (int i=0;i<char1.length;i++){
            char1[i]=s.charAt(i);
            char2[i]=t.charAt(i);

        }
        Arrays.sort(char1);
        Arrays.sort(char2);
        for(int i=0;i<s.length();i++){
            if(char1[i]!=char2[i]){
                return false;
            }
        }
        return true;
    }
}