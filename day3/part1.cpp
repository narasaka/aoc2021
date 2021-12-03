#include <bits/stdc++.h>
#define debug(x) cerr << #x << ": " << x << '\n'
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define sz(x) (int)(x).size()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
using namespace std;
using pi = pair<int, int>;
using ll = long long;

int convert(string s){
	int len = sz(s);
	int mul = 1;
	int res = 0;
	for(int i = len-1; i>=0; --i){
		if(s[i]=='1') res += mul;
		mul *= 2;
	}

	return res;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);

	string inp;
	cin >> inp;
	int len = sz(inp);

	vector<int> res(len, 0);
	for(int i = 0; i<len; ++i) if(inp[i]=='1') res[i]=1;

	int num = 1;
	while(cin >> inp){
		int idx = 0;
		for(auto c : inp){
			if(c=='1') res[idx]++;
			idx++;
		}
		num++;
	}

	string gamma(len, '0');
	string epsilon(len, '0');
	for(int i = 0; i<len; ++i){
		if(res[i]>num/2) gamma[i]='1';
		else epsilon[i]='1';
	}

	debug(gamma);
	debug(epsilon);
	for(int r : res) cout << r << ' ';
	cout << '\n';
	cout << convert(gamma)*convert(epsilon);
	
	return 0;
}
