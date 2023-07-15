#include <vector>
#include <algorithm>

class Solution {
public:
    int solve(int i, int k) {
        // Base cases
        if (i >= events.size()) {
            return 0;
        }
        if (k <= 0) {
            return 0;
        }
        
        // Check if the result for this state is already cached
        if (cache[i][k] != -1) {
            return cache[i][k];
        }
        
        // Retrieve start time, end time, and value of current event
        int start = events[i][0];
        int end = events[i][1];
        int value = events[i][2];
        
        // Find the next event that starts after the current event ends
        int nextIndex = i + 1;
        while (nextIndex < events.size() && events[nextIndex][0] <= end) {
            nextIndex++;
        }
        
        // We have two options: either take the current event or don't
        int takeEvent = value + solve(nextIndex, k - 1);
        int skipEvent = solve(i + 1, k);
        
        // Cache the result for this state
        cache[i][k] = std::max(takeEvent, skipEvent);
        
        return cache[i][k];
    }

    int maxValue(std::vector<std::vector<int>>& events, int k) {
        // Sort events based on their start times
        std::sort(events.begin(), events.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Store events for access within solve function
        this->events = events;
        
        // Clear cache before each function call
        cache.assign(events.size(), std::vector<int>(k + 1, -1));
        
        // Recursive call to solve the problem
        return solve(0, k);
    }
    
private:
    std::vector<std::vector<int>> events;
    std::vector<std::vector<int>> cache;
};