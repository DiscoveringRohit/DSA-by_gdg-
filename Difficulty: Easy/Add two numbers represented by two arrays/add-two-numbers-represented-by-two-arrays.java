class Solution {
    String calc_Sum(int arr1[], int arr2[]) {

        int i = arr1.length - 1;
        int j = arr2.length - 1;
        int carry = 0;

        StringBuilder sb = new StringBuilder();

        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;

            if (i >= 0) sum += arr1[i--];
            if (j >= 0) sum += arr2[j--];

            sb.append(sum % 10);
            carry = sum / 10;
        }

        return sb.reverse().toString();
    }
}
