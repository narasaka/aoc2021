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

	int ans = 0;
	int a, b, c;

	cin >> a >> b >> c;
	int init_sum = a+b+c;

	int temp;
	while(cin >> temp){
		a = b;
		b = c;
		c = temp;
		int new_sum = a+b+c;
		if(new_sum > init_sum) ans++;
		init_sum = new_sum;
	}

	cout << ans;

	return 0;
}