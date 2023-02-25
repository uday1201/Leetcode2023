#include <iostream>
using namespace std;

class node
{
	public:
	int data;
	node* left;
	node* right;
};

node* NodeGenrator(int data)
{
	node* Node = new node();
	Node->data = data;
	Node->left = NULL;
	Node->right = NULL;
	
	return(Node);
}

int maxDepth(node* node)
{
	if (node == NULL)
		return -1;
	else
	{

		int lDepth = maxDepth(node->left);
		int rDepth = maxDepth(node->right);
	
		if (lDepth > rDepth)
			return(lDepth + 1);
		else return(rDepth + 1);
	}
}
	
int main()
{
	node *root = NodeGenrator(1);

	root->left = NodeGenrator(2);
	root->right = NodeGenrator(3);
	root->left->left = NodeGenrator(4);
	root->left->right = NodeGenrator(5);
    root->left->left->left = NodeGenrator(6);
	root->left->right->right = NodeGenrator(7);

    int maxdepth = maxDepth(root);

	cout << "Height of tree is " << maxdepth << endl;
	return 0;
}

