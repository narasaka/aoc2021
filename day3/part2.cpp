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

	vector<string> vals;
	string inp;
	while(cin >> inp) vals.pb(inp);

	int ox, co;
	vector<string> oxv(vals.begin(), vals.end());
	vector<string> cov(vals.begin(), vals.end());
	
	int idx = 0;
	while(sz(oxv)!=1){
		vector<string> temp;
		int ones = 0, zeros = 0;
		for(auto val : oxv){
			if(val[idx]=='1') ones++;
			else zeros++;
		}

		char bit = (ones >= zeros ? '1' : '0');
		for(auto val : oxv) if(val[idx]==bit) temp.pb(val);
		oxv = vector<string>(temp.begin(), temp.end());
		idx++;
	}
	ox = convert(oxv[0]);

	idx = 0;
	while(sz(cov)!=1){
		vector<string> temp;
		int ones = 0, zeros = 0;
		for(auto val : cov){
			if(val[idx]=='1') ones++;
			else zeros++;
		}

		char bit = (ones >= zeros ? '0' : '1');
		for(auto val : cov) if(val[idx]==bit) temp.pb(val);
		cov = vector<string>(temp.begin(), temp.end());
		idx++;
	}
	co = convert(cov[0]);

	cout << ox*co;

	return 0;
}
