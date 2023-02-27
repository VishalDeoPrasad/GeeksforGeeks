class Solution {
    static String conRevstr(String S1, String S2) {
        String S = S1+S2;
        
        StringBuffer sb=new StringBuffer(S);
        String rev=sb.reverse().toString(); 

        return rev;
    }
}