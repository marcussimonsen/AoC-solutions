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

    bool report_safe = true;

    for (int j = 0; j < report.size(); j++) {
      int deleted = report[j];
      report.erase(report.begin() + j);

      int first_diff = report[1] - report[0];
      report_safe = true;

      for (int i = 1; i < report.size(); i++) {
        int diff = report[i] - report[i - 1];
        if (abs(diff) > 3 || first_diff * diff <= 0) {
          report_safe = false;
          break;
        }
      }
      report.insert(report.begin() + j, deleted);
      if (report_safe) {
        safe_reports++;
        break;
      }
    }
  }

  cout << safe_reports << endl;
}
