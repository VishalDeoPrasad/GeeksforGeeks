vector<vector<int>> transpose(int a[][M], int n)
{
    vector<vector<int>> v(n, vector<int>(M));

    for(int i=0;i<n;i++){

        for(int j=0;j<M;j++){

              v[i][j]=a[j][i];

        }

    }

    return v;
}