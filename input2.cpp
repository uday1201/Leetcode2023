// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <sstream>
using namespace std;

// Data structure to store a graph edge
struct Edge {
	int src, dest;
};

int main(){
    vector<Edge> edges = {};
    int target;
    int n = 0;
    string filename = "input.txt";
    std::ifstream inFile(filename);

    std::string line;

    while(std::getline(inFile, line)){
        if(!line.compare("*")){
            continue;
            cout << "*"<<endl;
        }
        else if(!line.compare("#")){
            break;
        }
        std::stringstream ss(line);
        std::string first, second;
        std::getline(ss,first,',');
        std::getline(ss,second,',');
        if(!second.empty()){
            edges.push_back({stoi(first), stoi(second)});
            cout << stoi(first) << ", " << stoi(second) << endl;
            n++;
        }
        else{
            target = stoi(first);
            cout<< target<< endl;
        }
    
        }
    cout<< n << endl;

}

