#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    vector<int> pos(n + 1);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        pos[arr[i]] = i;
    }

    int curr = 0;
    while (curr < (n + 1) / 2)
    {
        int i = pos[curr + 1];

        for (int o = i; o > curr; o--)
        {
            arr[o] = arr[o - 1];
            pos[arr[o]] = o;
        }
        arr[curr] = curr + 1;
        pos[curr + 1] = curr;
        cout << i - curr;
        cout << endl;

        if (curr + 1 != n - curr)
        {

            int i = pos[n - curr];
            for (int o = i; o < n - curr - 1; o++)
            {
                arr[o] = arr[o + 1];
                pos[arr[o]] = o;
            }
            cout << (n - curr - 1) - i;
            cout << endl;
            arr[n - curr - 1] = n - curr;
        }
        curr = curr + 1;
    }
    return 0;
}