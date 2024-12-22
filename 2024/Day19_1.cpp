#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

map<string, bool> cache;

vector<string> parse_towels(string &input) {
  vector<string> result;
  istringstream stream(input);
  string token;

  while (getline(stream, token, ',')) {
    // Trim leading and trailing spaces
    size_t start = token.find_first_not_of(" ");
    size_t end = token.find_last_not_of(" ");
    if (start != string::npos && end != string::npos) {
      token = token.substr(start, end - start + 1);
    }

    result.push_back(token);
  }

  return result;
}

bool can_make(string pattern, vector<string> &towels) {
  if (pattern.size() == 0)
    return true;

  if (cache.find(pattern) != cache.end())
    return cache[pattern];

  for (string towel : towels) {
    // Check if towel is prefix of pattern
    for (int i = 0; i < towel.size(); i++) {
      if (towel[i] != pattern[i]) {
        goto skip_towel;
      }
    }

    // Check if rest of pattern can be made
    if (can_make(pattern.substr(towel.size()), towels)) {
      cache[pattern] = true;
      return true;
    }
  skip_towel:
  }
  cache[pattern] = false;
  return false;
}

int main() {
  string line;
  vector<string> towels;
  vector<string> patterns;

  if (!getline(cin, line)) {
    cout << "Couldn't read towels!" << endl;
    return 1;
  }

  // Process towels
  towels = parse_towels(line);

  getline(cin, line);

  // Read patterns
  while (getline(cin, line)) {
    patterns.push_back(line);
  }

  int makeable_patterns = 0;

  for (string pattern : patterns) {
    cout << pattern;
    if (can_make(pattern, towels)) {
      makeable_patterns++;
      cout << " possible" << endl;
    } else {
      cout << " impossible" << endl;
    }
  }

  cout << "Makeable patterns: " << makeable_patterns << endl;

  return 0;
}
