class Solution{   
public:
    string compareNum(int A,int B){
        if (A==B){
            cout<<A<<" is equals to "<<B; 
        }
        else if(A>B){
            cout<<A<<" is greater than "<<B; 
        }
        else{
            cout<<A<<" is less than "<<B; 
        } 
    }
};