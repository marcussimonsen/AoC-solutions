#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  vector<int> middle_numbers = {};
  map<int, vector<int>> rules;
  string line;

  while (getline(cin, line)) {
    int a, b;
    if (sscanf(line.c_str(), "%d|%d", &a, &b) == 2)
      rules[a].push_back(b);
    else
      break;
  }

  while (getline(cin, line)) {
    vector<int> update;
    int a;
    char c;
    stringstream s;

    for (char c : line) {
      if (c == ',') {
        s << ' ';
      } else {
        s << c;
      }
    }

    while (s >> a) {
      update.push_back(a);
    }

    bool update_was_invalid = false;
  fix_update:
    for (int i = 1; i < update.size(); i++) {
      for (int j = i - 1; j >= 0; j--) {
        for (int k = 0; k < rules[update[i]].size(); k++) {
          if (rules[update[i]][k] == update[j]) {
            update_was_invalid = true;
            int tmp = update[i];
            update[i] = update[j];
            update[j] = tmp;
            goto fix_update;
          }
        }
      }
    }
    if (update_was_invalid) {
      middle_numbers.push_back(update[update.size() / 2]);
    }
  }

  int sum = 0;
  for (int i = 0; i < middle_numbers.size(); i++) {
    sum += middle_numbers[i];
  }
  cout << "Sum: " << sum << endl;

  return 0;
}
