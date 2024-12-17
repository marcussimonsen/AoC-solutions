#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  long long total_calibration_result = 0;
  string line;
  char colon;

  while (getline(cin, line)) {
    stringstream s(line);

    long long result;
    vector<long long> equation = {};
    long long num;

    s >> result;
    s >> colon;
    while (s >> num) {
      equation.push_back(num);
    }

    bool solves = false;
    for (int i = 0; i <= pow(3, equation.size() - 1); i++) {
      long long res = equation[0];
      for (int j = 1; j < equation.size(); j++) {
        long long op = i / pow(3, j-1);
        if (op % 3LL == 0LL) {
          res *= equation[j];
        } else if (op % 3LL == 1LL) {
          res += equation[j];
        } else {
          res = stoll(to_string(res) + to_string(equation[j]));
        }
      }
      if (res == result) {
        solves = true;
        break;
      }
    }

    if (solves) {
      total_calibration_result += result;
    }
  }

  cout << "Total calibration result: " << total_calibration_result << endl;

  return 0;
}
