
struct T {
    int weight;
    int index;
    long long freeTime;
};

class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        int n = servers.size();
        int m = tasks.size();

        vector<int> ans(m);

        auto compareFree = [](const T& a, const T& b) {
            return a.weight == b.weight
                ? a.index > b.index
                : a.weight > b.weight;
        };

        auto compareUsed = [](const T& a, const T& b) {
            if (a.freeTime != b.freeTime)
                return a.freeTime > b.freeTime;

            if (a.weight != b.weight)
                return a.weight > b.weight;

            return a.index > b.index;
        };

        priority_queue<T, vector<T>, decltype(compareFree)> free(compareFree);

        priority_queue<T, vector<T>, decltype(compareUsed)> used(compareUsed);

        for (int i = 0; i < n; i++) {
            free.push({servers[i], i, 0});
        }

        for (int i = 0; i < m; i++) {

            long long currentTime = i;

            while (!used.empty() &&
                   used.top().freeTime <= currentTime) {
                free.push(used.top());
                used.pop();
            }

            if (free.empty()) {
                T server = used.top();
                used.pop();

                ans[i] = server.index;

                server.freeTime += tasks[i];

                used.push(server);
            }
            else {
                T server = free.top();
                free.pop();

                ans[i] = server.index;

                server.freeTime = currentTime + tasks[i];

                used.push(server);
            }
        }

        return ans;
    }
};
