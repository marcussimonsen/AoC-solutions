#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string input;

  int safe_reports = 0;

  while (getline(cin, input)) {
    int a;
    vector<int> report;
    istringstream iss(input);
    while (iss >> a) {
      report.push_back(a);
    }

    int first_diff = report[1] - report[0];
    bool report_safe = true;

    for (int i = 1; i < report.size(); i++) {
      int diff = report[i] - report[i-1];
      if (abs(diff) > 3 || first_diff * diff <= 0) {
        report_safe = false;
        break;
      }
    }

    if (report_safe)
      safe_reports++;
  }

  cout << safe_reports << endl;
}
