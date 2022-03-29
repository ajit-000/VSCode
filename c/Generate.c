#include <bits/stdc++.h>
using namespace std;
int main()
{
    int tt = 0;
    string ss;
    string num = "";
    string num1 = "";
    getline(cin, ss);
    transform(ss.begin(), ss.end(), ss.begin(), ::tolower);
    int n = ss.length();
    string c;
    getline(cin, c);
    transform(c.begin(), c.end(), c.begin(), ::tolower);
    string num2 = "";
    int m = c.length();

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (ss[i] == ss[j])
            {
                tt = 1;
            }
        }
    }

    string w = "";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (ss[i] == c[j])
            {
                w += ss[i];
            }
        }
    }
    int g = w.length();

    for (int i = 0; i < g; i++)
    {
        if (w[i] - '0' >= 0 and w[i] - '0' <= 9)
        {
            num += w[i];
        }
    }
    for (int i = 0; i < g; i++)
    {
        if (isdigit(w[i]))
        {
            w.erase(i, 1);
            i--;
        }
    }
    if (tt == 0)
    {
        cout << w << " " << num;
    }
    else
    {
        cout << "New Language Error";
    }
    return 0;
}