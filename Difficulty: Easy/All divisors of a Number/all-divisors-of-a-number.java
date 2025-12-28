class Solution {
    public static void print_divisors(int n) {
        ArrayList<Long> small = new ArrayList<>();
        ArrayList<Long> large = new ArrayList<>();

        for (long i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                small.add(i);
                if (i != n / i) {
                    large.add(n / i);
                }
            }
        }
        for (long x : small) {
            System.out.print(x + " ");
        }
        for (int i = large.size() - 1; i >= 0; i--) {
            System.out.print(large.get(i) + " ");
        }
    }

    public static void main(String[] args) {
    print_divisors(20);
    
    }
}
