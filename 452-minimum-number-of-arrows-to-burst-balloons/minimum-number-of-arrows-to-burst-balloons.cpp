class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0)
            return 0;
        
        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b){
            return a[1] < b[1];
        });
        
        int arrowCount = 0;
        long long possibleEnd = LLONG_MIN;
        
        for (const auto& p : points) {
            if (p[0] > possibleEnd) {
                possibleEnd = p[1];
                arrowCount += 1;
            }
        }
        
        return arrowCount;   
    }
};