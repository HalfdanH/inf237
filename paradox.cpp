#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <stack>
#include <algorithm>
#include <queue>
#include <unordered_map>
using namespace std;

int Pos21D(std::pair<int, int> Pos, std::pair<int, int> MapDimensions)
{
    return Pos.second * MapDimensions.first + Pos.first;
}
std::pair<int, int> Pos12D(int Pos, std::pair<int, int> MapDimensions)
{
    return {Pos % MapDimensions.first, Pos / MapDimensions.first};
}
bool valid(std::pair<int, int> Pos, const std::vector<int> &Map, std::pair<int, int> MapDimensions)
{
    if (Pos.second >= 0 and Pos.second < MapDimensions.second and Pos.first >= 0 and Pos.first < MapDimensions.first and Map[Pos21D(Pos, MapDimensions)] == 1)
    {
        return true;
    }
    return false;
}
vector<pair<int, int>> Neighbours(std::pair<int, int> Pos,
                                  const std::vector<int> &Map,
                                  std::pair<int, int> MapDimensions,
                                  std::vector<int> &Parents)
{
    std::vector<pair<int, int>> Neighs;

    std::pair<int, int> neigh1(Pos.first + 1, Pos.second);
    std::pair<int, int> neigh2(Pos.first - 1, Pos.second);
    std::pair<int, int> neigh3(Pos.first, Pos.second + 1);
    std::pair<int, int> neigh4(Pos.first, Pos.second - 1);
    if (valid(neigh1, Map, MapDimensions) and Parents[Pos21D(neigh1, MapDimensions)] == -1)
    {
        Neighs.emplace_back(neigh1);
    }
    if (valid(neigh2, Map, MapDimensions) and Parents[Pos21D(neigh2, MapDimensions)] == -1)
    {
        Neighs.emplace_back(neigh2);
    }
    if (valid(neigh3, Map, MapDimensions) and Parents[Pos21D(neigh3, MapDimensions)] == -1)
    {
        Neighs.emplace_back(neigh3);
    }
    if (valid(neigh4, Map, MapDimensions) and Parents[Pos21D(neigh4, MapDimensions)] == -1)
    {
        Neighs.emplace_back(neigh4);
    }
    return Neighs;
}

bool FindPath(std::pair<int, int> Start,
              std::pair<int, int> Target,
              const std::vector<int> &Map,
              std::pair<int, int> MapDimensions,
              std::vector<int> &OutPath)
{
    if (Start == Target)
    {
        return true;
    }
    if (Map.empty())
    {
        return false;
    }

    std::vector<int> Parents(Map.size(), -1);
    Parents[Pos21D(Start, MapDimensions)] = -2;
    std::queue<pair<int, int>> q;
    q.push(Start);
    std::pair<int, int> curr;
    std::vector<std::pair<int, int>> neighs;
    std::pair<int, int> par;
    while (!q.empty())
    {
        curr = q.front();
        if (curr == Target)
        {
            while (curr != Start)
            {
                OutPath.emplace_back(Pos21D(curr, MapDimensions));
                curr = Pos12D(Parents[Pos21D(curr, MapDimensions)], MapDimensions);
            }
            std::reverse(OutPath.begin(), OutPath.end());
            return true;
        }
        q.pop();
        neighs = Neighbours(curr, Map, MapDimensions, Parents);
        for (pair<int, int> n : neighs)
        {
            Parents[Pos21D(n, MapDimensions)] = Pos21D(curr, MapDimensions);
            q.push(n);
        }
    }

    return false;
}

std::vector<int> Map;
std::vector<int> Map1 = {1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1};
std::vector<int> Map2 = {1, 1, 1, 1, 1,
                         0, 0, 0, 0, 1,
                         1, 1, 1, 1, 1,
                         1, 0, 0, 0, 0,
                         1, 1, 1, 1, 1};
std::vector<int> OutPath;
int main()
{

    bool a = FindPath({0, 0}, {4, 4}, Map2, {5, 5}, OutPath);
    for (int i : OutPath)
    {
        std::cout << i << "\n";
    }
    std::cout << a;
    return 0;
}
