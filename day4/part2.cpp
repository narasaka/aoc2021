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

bool win(vector<pair<int, bool>> board){
	// check horizontal
	for(int i = 0; i<25; i+=5){
		bool won = true;
		for(int j = 0; j<5; ++j){
			if(!board[i+j].second){
				won = false;
				break;
			}
		}
		if(won) return true;
	}

	//check vertical
	for(int i = 0; i<5; ++i){
		bool won = true;
		for(int j = 0; j<25; j+=5){
			if(!board[i+j].second){
				won = false;
				break;
			}
		}
		if(won) return true;
	}

	return false;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);

	vector<int> calls;
	string str_calls;
	cin >> str_calls;

	replace(str_calls.begin(), str_calls.end(), ',', ' ');
	stringstream ss(str_calls);

	int temp;
	while(ss >> temp) calls.pb(temp);

	vector<pair<vector<pair<int, bool>>, bool>> boards;
	vector<pair<int, bool>> temp_b;
	while(cin >> temp){
		temp_b.pb(mp(temp, false));
		if(sz(temp_b)==25){
			boards.pb(mp(temp_b, false));
			temp_b.clear();
		}
	}

	int wins = 0;
	for(int call : calls){
		for(auto &board : boards){
			for(auto &x : board.first){
				if(x.first==call) x.second = true;
			}

			if(win(board.first) && !board.second){
				wins++;
				board.second = true;
				if(wins==sz(boards)){
					int unmarked = 0;
					for(auto xx : board.first){
						if(!xx.second) unmarked += xx.first;
					}
					cout << unmarked*call;
					return 0;
				}
			}
		}
	}

	return 0;
}
