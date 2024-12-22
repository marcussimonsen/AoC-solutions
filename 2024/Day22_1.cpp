#include <iostream>
#include <vector>
using namespace std;

long long step(long long num) {
  long long n;

  n = num * 64;
  n ^= num;
  n %= 16777216ll;
  num = n;

  n = num / 32;
  n ^= num;
  n %= 16777216ll;
  num = n;

  n = num * 2048;
  n ^= num;
  n %= 16777216ll;
  num = n;

  return n;
}

int main() {
  vector<long long> secret_numbers;
  long long num;
  long long res = 0;

  while (cin >> num) {
    secret_numbers.push_back(num);
  }


  for (long long n : secret_numbers) {
    num = n;
    for (int i = 0; i < 2000; i++) {
      num = step(num);
    }
    res += num;
  }

  cout << "Sum of secret numbers: " << res << endl;

  return 0;
}
