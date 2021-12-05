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

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);

	vector<vector<int>> floor(10000, vector<int>(10000, 0));
	string a, b, arrow;
	while(cin >> a >> arrow >> b){
		int x1, x2, y1, y2;
		replace(all(a), ',', ' ');
		replace(all(b), ',', ' ');
		stringstream ssa(a);
		stringstream ssb(b);
		ssa >> x1 >> y1;
		ssb >> x2 >> y2;

		if(x1==x2){
			for(int i = min(y1, y2); i<=max(y1, y2); ++i){
				floor[i][x1]++;
			}
		}

		if(y1==y2){
			for(int i = min(x1, x2); i<=max(x1, x2); ++i){
				floor[y1][i]++;
			}
		}

		if(abs(y2-y1)==abs(x2-x1)){
			int i = y1, j = x1;
			while(i != y2){
				floor[i][j]++;

				if(y1<y2) i++;
				else i--;

				if(x1<x2) j++;
				else j--;
			}
			floor[i][j]++;
		}
	}

	int ans = 0;
	for(auto f : floor)
		for(auto x : f)
			if(x>=2) ans++;

	cout << ans;

	return 0;
}
