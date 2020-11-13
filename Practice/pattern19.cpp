// # 5 -> input
// #     1
// #    121
// #   12321
// #  1234321
// # 123454321

#include<iostream>
using namespace std;

int main(void){
int n;
cin>>n;
int space=n-1;
int num=1;


for(int i=0;i<n;i++)
{
    for(int j=0;j<space;j++)
    {
        cout<<" ";
    }
    int count=1;
    for(int k=0;k<num;k++)
    {
        cout<<count;
        if (k<num/2){
            count++;
        }
        else
        {
            count--;
        }
        
    }
    num+=2;
    cout<<endl;
    space--;
}

}


