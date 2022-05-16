#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
vector<bool>visit;

void edge(vector<int>adj[],int u,int v)
{
    adj[u].push_back(v);
}
void bfs(int s,vector<int>adj[])
{
    queue<int>q;
    q.push(s);
    visit[s]=true;
    while(!q.empty())
    {
        int u=q.front();
        cout<<u<<" ";
        q.pop();
        
        for(int i=0;i<adj[u].size();i++){
            if(!visit[adj[u][i]])
            {
                q.push(adj[u][i]);
                visit[adj[u][i]]=true;
            }
        }
    }
}
void dfs(int s,vector<int>adj[])
{
    stack<int>st;
    st.push(s);
    visit[s]=true;
    while(!st.empty())
    {
        int u=st.top();
        cout<<u<<" ";
        st.pop();
        
        for(int i=0;i<adj[u].size();i++){
            if(!visit[adj[u][i]])
            {
                st.push(adj[u][i]);
                visit[adj[u][i]]=true;
            }
        }
    }
}
int main()
{
    visit.assign(5,false);
    vector<int>adj[5];
    edge(adj,0,2);
    edge(adj,0,1);
    edge(adj,1,3);
    edge(adj,2,0);
    edge(adj,2,3);
    edge(adj,2,4);
    
    cout<<"bfs"<<" "<<endl;
    bfs(0,adj);
    cout<<endl;
    
     visit.assign(5,false);
    cout<<"dfs"<<" "<<endl;
    dfs(0,adj);
    cout<<endl;
    
}
