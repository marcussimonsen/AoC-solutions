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

long long buy_bananas(vector<long long> &changes,
                      vector<long long> &secret_numbers,
                      vector<long long> &sequence) {
  /*for (auto l : sequence)*/
  /*  cout << l << " ";*/
  /*cout << endl;*/
  for (size_t i = 0ll; i < changes.size() - 3ll; i++) {
    for (size_t j = 0ll; j < 4ll; j++) {
      if (changes[i + j] != sequence[j]) {
        break;
      }
      if (j == 3) {
        /*cout << "Found sequence with value: " << secret_numbers[i + j] % 10ll
         * << endl;*/
        return secret_numbers[i + j] % 10ll;
      }
    }
  }
  return 0ll;
}

long long solve(vector<vector<long long>> &changes,
                vector<vector<long long>> &secret_numbers) {
  long long total_iterations = 19 * 19 * 19 * 19;
  long long current_iteration = 0;
  long long best = 0;
  for (long long a = -9ll; a < 10ll; a++) {
    for (long long b = -9ll; b < 10ll; b++) {
      for (long long c = -9ll; c < 10ll; c++) {
        for (long long d = -9ll; d < 10ll; d++) {
          current_iteration++;
          // (small) Optimization
          long long sum = a + b + c + d;
          if (sum < -10 || sum > 10)
            continue;

          long long bananas = 0ll;
          vector<long long> seq = {a, b, c, d};
          for (size_t i = 0; i < changes.size(); i++) {
            bananas += buy_bananas(changes[i], secret_numbers[i], seq);
          }
          best = max(best, bananas);
          cout << "\r" << (double(current_iteration) / total_iterations) * 100 << " %" << flush;
        }
      }
    }
  }
  return best;
}

int main() {
  vector<long long> initial_secret_numbers;
  vector<vector<long long>> secret_numbers;
  vector<vector<long long>> changes;
  long long num;
  long long res = 0;

  while (cin >> num) {
    initial_secret_numbers.push_back(num);
  }

  for (long long n : initial_secret_numbers) {
    vector<long long> c;
    vector<long long> nums;
    long long a = n;
    long long b;
    for (int i = 0; i < 2000; i++) {
      b = step(a);
      c.push_back(b % 10ll - a % 10ll);
      nums.push_back(b);
      a = b;
    }
    changes.push_back(c);
    secret_numbers.push_back(nums);
  }

  long long bananas = solve(changes, secret_numbers);

  cout << "Maximum bananas: " << bananas << endl;

  return 0;
}
