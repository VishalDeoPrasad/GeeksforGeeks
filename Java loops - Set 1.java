class Solution{
    static ArrayList<Integer> getSum(int N){
        int odd = 0;
        int even = 0;
        ArrayList<Integer> output= new ArrayList<>();
        for (int i=1; i<=N; i++){
            if (i%2 == 0){
                even = even+i;
            }
            else{
                odd = odd+i;
            }
        }
        output.add(even);
        output.add(odd);
        return output;
    }
}