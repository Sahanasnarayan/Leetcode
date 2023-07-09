class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
int column=matrix[0].size()-1;
        int row=0;
        while(row<matrix.size() && column>=0)
        {
            if(matrix[row][column]==target)
            return true;

            else if(matrix[row][column]>target)
            {
                --column;
            }
            else
            row++;
        }
        return false;
        
    }
};