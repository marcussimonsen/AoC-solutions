#include <cstdio>
#include <iostream>
#include <regex>
using namespace std;

int main() {
  int res = 0;
  string line;
  regex pattern("mul\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)");

  string program = "";

  while (getline(cin, line)) {
    program += line;
  }

  sregex_iterator begin(program.begin(), program.end(), pattern);
  sregex_iterator end;

  for (auto it = begin; it != end; ++it) {
    string instruction = it->str();
    if (instruction.find("don't") != string::npos) {
      while (it != end && instruction.find("do()") == string::npos) {
        ++it;
        instruction = it->str();
      }
      if (it == end)
        break;
      else
        continue;
    }
    if (instruction.find("do()") != string::npos)
      continue;
    smatch match;
    if (regex_match(instruction, match, pattern)) {
      int a = stoi(match[1]);
      int b = stoi(match[2]);
      res += a * b;
    } else {
      cout << "Error: Non-matching match" << endl;
    }
  }

  cout << res << endl;
}
