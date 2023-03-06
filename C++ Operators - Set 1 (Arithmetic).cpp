class Solution {
  public:
    vector<int> cppOperators(int A, int B) {
        vector<int>result;
        result.push_back(A+B);
        result.push_back(A*B);
        if (A>B){
            result.push_back(A-B);
            result.push_back(A/B);
        }
        else{
            result.push_back(B-A);
            result.push_back(B/A);
        }
        
        
        return result;
    }
};