class Solution {
    static boolean armstrongNumber(int n) {
        int sum_digit=0;
        int original=n;
        while(n>0){
            int digit=n%10;
            int powerNumber=digit*digit*digit;
            sum_digit=sum_digit+powerNumber;
            n/=10;
           
            
        }
        return sum_digit==original;
                
        
       
    }
}