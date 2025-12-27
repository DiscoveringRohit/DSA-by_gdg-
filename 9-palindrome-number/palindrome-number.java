class Solution {
    public boolean isPalindrome(int x) {
        int temp=0;
        int ori_number=x;
        while(x>0){
            int digit=x%10;
            x/=10;
            temp=temp*10+digit;
           
        }
         if(temp==ori_number){
                return true;
            }
        return false;
}    
    }
    