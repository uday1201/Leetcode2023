#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

struct Point { int x, y; };
Point closest1;
Point closest2;
bool compareX (Point p, Point q) { return p.x < q.x; }
bool compareY (Point p, Point q) { return p.y < q.y; }
float dist(Point p1, Point p2) {
    return sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y));
}

double min_dist (vector<Point> pointsX, vector<Point> pointsY, int n) {
     // BASE CASE.
    if (n <= 3) {
        double min = __DBL_MAX__;
        for (int i = 0; i < n; ++i)
            for (int j = i +1 ; j < n; ++j)
                if (dist(pointsX[i], pointsX[j]) < min){
                    min = dist(pointsX[i], pointsX[j]);
                    closest1.x = pointsX[i].x;
                    closest1.y = pointsX[i].y;
                    closest2.x = pointsX[j].x;
                    closest2.y = pointsX[j].y;
                }
        return min;
    }

    // Step 1: Find the middle point.
    int mid = n/2;
    Point mid_point = pointsX[mid];

    // Step 2: Divide the set in two equal-sized parts (left and right).
    vector<Point> pointsY_left;
    vector<Point> pointsY_right;
    vector<Point> pointsX_left;
    vector<Point> pointsX_right;

    for (int i = 0; i < n; ++i) {
        if (i < mid  and pointsY[i].x <= mid_point.x)  pointsY_left.push_back(pointsY[i]);
        else pointsY_right.push_back(pointsY[i]);
    }
    for (int i = 0; i < n; ++i) {
        if (i < mid and pointsX[i].x <= mid_point.x) pointsX_left.push_back(pointsX[i]);
        else pointsX_right.push_back(pointsX[i]);
    }

    // Step 3: Calculate the smaller distance at left and right parts recursively.
    double d_left = min_dist(pointsX_left, pointsY_left, mid);
    double d_right = min_dist(pointsX_right , pointsY_right, n - mid);

    // Let d be the minimal of the 2 distances.
    double d = min (d_left, d_right);

   // Eliminate points that are farther than d <=> Create a strip that contains
   // points closer than d.
   vector<Point> strip;
   for (int i = 0; i < n; ++i) if (abs(pointsY[i].x - mid_point.x) < d) strip.push_back(pointsY[i]);

   // Scan the points from the strip and compute the dstances of each point to its 7 neighbours.
   // Pick all points one by one and try the next points until the difference
   // between y coordinates is smaller than d.
   for (int i = 0; i < int(strip.size()); ++i)
        for (int j = i + 1; j < int(strip.size()) and (strip[j].y - strip[i].y) < d; ++j)
             if (dist (strip[i], strip[j]) < d)
             d = dist(strip[i], strip[j]);

     return d;
}

double closest(const vector<Point>& points) {
    // Initial step: sort points accroding to their coordinates.
    vector<Point> pointsX, pointsY;
    pointsX = pointsY = points;
    sort(pointsX.begin(), pointsX.end(), compareX);
    sort(pointsY.begin(), pointsY.end(), compareY);

    return min_dist (pointsX, pointsY, int(points.size()));
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(5);

    vector<Point> points = {};

    // Reading the input from the file
    string filename = "input.txt";
    std::ifstream inFile(filename);
    
    // reading one line at a time
    std::string line;

    // read lines until the EOF
    while(std::getline(inFile, line)){
         if(!line.compare("$")){
            break;
        }
        // else read the line and split it from the ,
        std::stringstream ss(line);
        std::string first, second;
        std::getline(ss,first,',');
        std::getline(ss,second,',');
        // If there are 2 numbers separated by comma, push them both to edges vector
        if(!second.empty()){
            points.push_back({stoi(first), stoi(second)});
            //cout << stoi(first) << ", " << stoi(second) << endl;
        }
    
    }

   cout << "Minimum distance is : " << closest (points) << endl;
   cout << "Closest points are : " << endl;
   cout << "(" << closest1.x << "," << closest1.y << ")" << endl ;
   cout << "(" << closest2.x << "," << closest2.y << ")" << endl ;
}