#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <map>
#include <vector>

using namespace std;

struct IntDefaultedToZero {
  int i = 0;
};

int main() {
  int a, b;
  vector<int> list_a;
  vector<int> list_b;

  while (scanf("%d %d", &a, &b) == 2) {
    list_a.push_back(a);
    list_b.push_back(b);
  }

  map<int, IntDefaultedToZero> occurrences;

  for (int i = 0; i < list_b.size(); i++) {
    IntDefaultedToZero val = occurrences[list_b[i]];
    val.i += 1;
    occurrences[list_b[i]] = val;
  }

  int total_similarity = 0;
  for (int i = 0; i < list_a.size(); i++) {
    total_similarity += list_a[i] * occurrences[list_a[i]].i;
  }

  cout << "Total similarity: " << total_similarity << endl;

  return 0;
}
