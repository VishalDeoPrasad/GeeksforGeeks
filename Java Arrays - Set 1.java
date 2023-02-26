class Compute
{
    String average(int A[], int N)
    {
        double sum = 0;
        for (int i=0; i<N; i++){
            sum += A[i];
        }
        return String.format("%.2f", sum/N);
    }
}