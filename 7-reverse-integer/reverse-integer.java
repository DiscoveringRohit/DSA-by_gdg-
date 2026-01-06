class Solution {
    public int reverse(int x) {
        long result=0;
        boolean neg=x<0;
        x=Math.abs(x);
        while (x>0){
            int digit=x%10;
            x=x/10;
            result=result*10+digit;
        }
        if (result>Integer.MAX_VALUE|| result<Integer.MIN_VALUE) return 0;
        if (neg) return (int)-result;
        return (int)result;
    }
}