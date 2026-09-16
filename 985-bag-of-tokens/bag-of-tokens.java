class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int n=tokens.length;
        int left=0;
        int right=n-1;
        int score=0;
        int maxScore=0;
        while (left<=right){
           
                 if (tokens[left]<=power){
                    power=power-tokens[left];
                    score+=1;
                    left++;
                    maxScore =Math.max(maxScore,score);
                 }
                
                    else if(score>=1){
                        power=power+tokens[right];
                        score--;
                        right--;
                    }
                    else{
                        break;
                    } 
        }

        return maxScore;
        
    }
}