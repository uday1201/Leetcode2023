
#include<iostream>
using namespace std;

int power(int x, unsigned int y)
{
	if (y == 0)
		return 1;
	else if (y % 2 == 0)
		return power(x, y / 2) * power(x, y / 2);
	else
		return x * power(x, y / 2) * power(x, y / 2);
}

int main()
{
	cout << power(3, 2) << endl;
	return 0;
}

