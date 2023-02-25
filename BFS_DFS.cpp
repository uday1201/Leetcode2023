#include <iostream>
#include <queue>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
using namespace std;
int target;
bool bfs, dfs;

// Data structure to store a graph edge
struct Edge {
	int src, dest;
};

// A class to represent a graph object
class Graph
{
public:
	// a vector of vectors to represent an adjacency list
	vector< vector<int> > adjList;

	// Graph Constructor
	Graph(vector<Edge> const &edges, int n)
	{
		// resize the vector to hold `n` elements of type `vector<int>`
		adjList.resize(n);

		// add edges to the undirected graph
		for (auto &edge: edges)
		{
			adjList[edge.src].push_back(edge.dest);
			adjList[edge.dest].push_back(edge.src);
		}
	}
};

// Perform BFS recursively on the graph
void recursiveBFS(Graph const &graph, queue<int> &q, vector<bool> &discovered)
{
	if (q.empty()) {
		return;
	}

	// dequeue front node and print it
	int v = q.front();
	q.pop();
	// cout << v << " ";

    if (v == target){
        bfs = true;
    }

	// do for every edge (v, u)
	for (int u: graph.adjList[v])
	{
		if (!discovered[u])
		{
			// mark it as discovered and enqueue it
			discovered[u] = true;
			q.push(u);
		}
	}

	recursiveBFS(graph, q, discovered);
}


// Function to perform DFS traversal on the graph on a graph
void DFS(Graph const &graph, int v, vector<bool> &discovered)
{
    // mark the current node as discovered
    discovered[v] = true;
 
    // print the current node
    // cout << v << " ";

    if (v == target){
        dfs = true;
    }
 
    // do for every edge (v, u)
    for (int u: graph.adjList[v])
    {
        // if `u` is not yet discovered
        if (!discovered[u]) {
            DFS(graph, u, discovered);
        }
    }
}


int main()
{
	// vector of graph edges as per the above diagram
	vector<Edge> edges = {};

	// total number of nodes in the graph
	int n = 1;

    // Reading the input from the file
    string filename = "input.txt";
    std::ifstream inFile(filename);
    
    // reading one line at a time
    std::string line;

    // read lines until the EOF
    while(std::getline(inFile, line)){
        // continue if *
        if(!line.compare("*")){
            continue;
        }
        // break if #
        else if(!line.compare("#")){
            break;
        }
        // else read the line and split it from the ,
        std::stringstream ss(line);
        std::string first, second;
        std::getline(ss,first,',');
        std::getline(ss,second,',');
        // If there are 2 numbers separated by comma, push them both to edges vector
        if(!second.empty()){
            edges.push_back({stoi(first), stoi(second)});
            // cout << stoi(first) << ", " << stoi(second) << endl;
            n++;
        }
        // Otherwise it is the target
        else{
            target = stoi(first);
            // cout<< target<< endl;
        }
    
    }

	// build a graph from the given edges
	Graph bgraph(edges, n);

	// to keep track of whether a vertex is discovered or not
	vector<bool> bdiscovered(n, false);

	// create a queue for doing BFS
	queue<int> q;

    // BFS start
    cout << "Performing Breadth First Search"<< endl;

	// Perform BFS traversal from all undiscovered nodes to
	// cover all connected components of a graph
    bfs = false;
	for (int i = 0; i < n; i++)
	{
		if (bdiscovered[i] == false)
		{
			// mark the source vertex as discovered
			bdiscovered[i] = true;

			// enqueue source vertex
			q.push(i);

			// start BFS traversal from vertex `i`
			recursiveBFS(bgraph, q, bdiscovered);
		}
	}

    // Check the bfs bool var to print success or failure
    if (bfs == true){
        cout << "Success -> Target found in BFS" << endl;
    }
    else{
        cout << "Failure -> Target not found in BFS" << endl;
    }

    // DFS start
    cout << "Performing Depth First Search" << endl;

    // build a graph from the given edges
	Graph dgraph(edges, n);

	// to keep track of whether a vertex is discovered or not
	vector<bool> ddiscovered(n, false);

    // Perform DFS traversal from all undiscovered nodes to
    // cover all connected components of a graph
    for (int i = 0; i < n; i++)
    {
        if (ddiscovered[i] == false) {
            DFS(dgraph, i, ddiscovered);
        }
    }

    // Check the bfs bool var to print success or failure
    if (dfs == true){
        cout << "Success -> Target found in DFS" << endl;
    }
    else{
        cout << "Failure -> Target not found in DFS" << endl;
    }

	return 0;
}