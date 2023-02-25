
using namespace std;
#include <iostream>
#include <bits/stdc++.h>

int locate_tower(int house[], int range, int n)
{
	// first we sort the house numbers
	sort(house, house + n);

	// for count number of towers
	int numOfTower = 0;

    cout << "Location of the towers - " ;

	// for iterate all houses
	int i = 0;
	while (i < n) {

		// count number of towers
		numOfTower++;

		// find find the middle location
		int loc = house[i] + range;

		// traverse till middle location
		while (i < n && house[i] <= loc)
			i++;

		// this is point to middle
		// house where we insert the tower
        cout << i << " - ";
		--i;

		// now find the last location
		loc = house[i] + range;

		// traverse till last house of the range
		while (i < n && house[i] <= loc)
			i++;
	}

	// return the number of tower
	return 0;
}

int main()
{
	int house[] = { 3, 9, 10, 15};
	int range = 4;
	int n = sizeof(house) / sizeof(house[0]);
	locate_tower(house, range, n);
}
