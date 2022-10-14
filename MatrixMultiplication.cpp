
#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    
        
    int dp[101][101];
    
    int helper(int arr[], int i, int j){
        
        if(i >= j){
            return 0;
        }
        
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        
        int mn = INT_MAX;
        
        for(int k = i; k < j; k++){
            
            int left, right;
            
            if(dp[i][k] != -1){
                left = dp[i][k];
            }
            else{
                left = helper(arr ,i ,k);
                dp[i][k] = left;
            }
            
            if(dp[k+1][j] != -1){
                 right =  dp[k+1][j];
            }
            else{
                right = helper(arr,k+1,j);
                dp[k+1][j] = right;
            }
            
            
            mn = min(mn, left + right + arr[i-1]*arr[k]*arr[j] );
            
        }
        
        return dp[i][j] = mn;
    }

    int matrixMultiplication(int n, int arr[])
    {
        for(int i = 0; i < 101; i++){
            for(int j = 0; j < 101; j++){
                dp[i][j] = -1;
            }
        }
        
        return helper(arr,1,n-1);
        
    }
};

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[N];
        for(int i = 0;i < N;i++)
            cin>>arr[i];
        
        Solution ob;
        cout<<ob.matrixMultiplication(N, arr)<<endl;
    }
    return 0;
}