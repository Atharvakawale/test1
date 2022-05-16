#include <iostream>
using namespace std;

int main()
{
    int n;
    int a[30];
    cout<<"Enter the number element you have to sort"<<endl;
    cin>>n;
    cout<<"Enter the numbers:";
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n-1;i++)
    {
        int min=a[i];
        int loc=i;
        
        for(int j=i;j<n;j++)
        {
            if(min>a[j])
            {
                min=a[j];
                loc=j;
            }
        } 
    int temp;
    temp=a[i];
    a[i]=a[loc];
    a[loc]=temp;
    }
    for(int k=0;k<n;k++)
        {
            cout<<a[k]<<" ";
        }
}
