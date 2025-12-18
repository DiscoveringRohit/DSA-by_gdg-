class Solution {
    public String frequencySort(String s) {
        int[] arr =new int[123];
        for(int i=0;i<s.length();i++){
            int ch=(int)s.charAt(i);
            arr[ch]++;
        }
        // Arrays.sort(arr);

        String a="";
        while(true){
            int i = max(arr);
            if(arr[i] == 0)
                break;
            if(i>=10){
                char ch=(char)(i);
                int times = arr[i];
                String add_s="";
                for(int j=0;j<times;j++){
                    add_s+=ch;
                }
                a+=add_s;
            }
            else{
                char ch=(char)i;
                int times = arr[i];
                String add_s="";
                for(int j=0;j<times;j++){
                    add_s+=ch;
                }
                a+=add_s;
            
            }
            arr[i] = 0;
        }
        return a; 
    }

    public int max(int [] arr){
        int max=arr[0];
        int ind=0;
        for (int i=0;i<arr.length;i++){
            if(arr[i]>max){
                max=arr[i];
                ind=i;
            }
        }
        return ind;
    }
}