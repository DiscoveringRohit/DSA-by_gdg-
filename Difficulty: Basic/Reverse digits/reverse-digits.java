// User function Template for Java

class Solution {
    public int reverseDigits(int n) {
        // Code here
        int temp=0;
            while(n>0){
                int digit=n%10;
                n/=10;
                temp=temp*10+digit;
              
                
            }  
            return temp;
            
    }
}