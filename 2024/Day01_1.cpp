#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
  int a, b;
  vector<int> list_a;
  vector<int> list_b;

  while (scanf("%d %d", &a, &b) == 2) {
    list_a.push_back(a);
    list_b.push_back(b);
  }

  sort(list_a.begin(), list_a.end());
  sort(list_b.begin(), list_b.end());

  int total_distance = 0;
  for (int i = 0; i < min(list_a.size(), list_b.size()); i++) {
    total_distance += abs(list_a[i] - list_b[i]);
  }

  cout << "Total distance: " << total_distance << endl;

  return 0;
}
