// Last updated: 10/2/2025, 12:21:08 PM
class Solution {
 public:
  int maxBottlesDrunk(int numBottles, int numExchange) {
    int ans = numBottles;

    while (numBottles >= numExchange) {
      numBottles = (numBottles - numExchange + 1);
      ++numExchange;
      ++ans;
    }

    return ans;
  }
};