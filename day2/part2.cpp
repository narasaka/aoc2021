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

	int x = 0, y = 0;
	int aim = 0;
	string dir;
	int n;

	while(cin >> dir >> n){
		if(dir=="forward"){
			x += n;
			y += aim*n;
		}else if(dir=="down"){
			aim += n;
		}else {
			aim -= n;
		}
	}

	cout << x*y;

	return 0;
}
