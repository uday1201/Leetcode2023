// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;

// Data structure to store a graph edge
struct Edge {
	int src, dest;
};

int main () {
  string line;
  ifstream myfile ("input.txt");
  vector<Edge> edges = {};
  int target;
  int test[2] = {};
  int n;
  char dump;
    myfile >> test[0];
    myfile >> dump;
    myfile >> test[1];
    edges.push_back({test[0], test[1]});
  if (myfile.is_open())
  {
    while ( getline (myfile,line))
    {   
        if (line == "*"){
            break;
        }
        else{
        myfile >> test[0];
        myfile >> dump;
        myfile >> test[1];
        edges.push_back({test[0], test[1]});
        n++;
        target = test[1];
        }
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 
  edges.pop_back();
  cout << target << endl;

  return 0;
}