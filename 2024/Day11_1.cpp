#include <cstdio>
#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
  long long s;
  list<long long> stones;

  while (scanf("%lld", &s) == 1) {
    stones.push_back(s);
  }

  for (int i = 0; i < 25; i++) {
    for (auto it = stones.begin(); it != stones.end(); ++it) {
      long long num = *it;
      string num_s = to_string(num);

      if (num == 0) {
        *it = 1;
      } else if (num_s.length() % 2 == 0) {
        int half_len = num_s.length() / 2;
        long long a = stoll(num_s.substr(0, half_len));
        long long b = stoll(num_s.substr(half_len, half_len));
        *it = b;
        stones.insert(it, a);
      } else {
        *it = *it * 2024;
      }
    }
  }

  cout << stones.size() << endl;

  return 0;
}
