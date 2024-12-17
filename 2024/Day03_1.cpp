#include <cstdio>
#include <iostream>
#include <regex>
using namespace std;

int main() {
  int res = 0;
  string line;
  string program = "";
  regex pattern("mul\\((\\d+),(\\d+)\\)");

  while (getline(cin, line)) {
    program += line;
  }

    sregex_iterator begin(program.begin(), program.end(), pattern);
    sregex_iterator end;

    for (auto it = begin; it != end; ++it) {
      string mul = it->str();
      smatch match;
      if (regex_match(mul, match, pattern)) {
        int a = stoi(match[1]);
        int b = stoi(match[2]);
        res += a * b;
      } else {
        cout << "Error: Non-matching match" << endl;
      }
    }
  cout << res << endl;
}
