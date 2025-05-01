#include <iostream>
#include <tuple>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <unordered_set>
#include <utility>
#include <algorithm>
using namespace std;
namespace std
{
    template <>
    struct hash<std::pair<double, double>>
    {
        size_t operator()(const std::pair<double, double> &p) const
        {
            return std::hash<double>{}(p.first) ^ (std::hash<double>{}(p.second) << 1);
        }
    };

}

auto round2 = [](double value)
{
    return std::round(value * 100.0) / 100.0;
};

double dist(pair<double, double> point1, pair<double, double> point2)
{
    double x_diff = point1.first - point2.first;
    double y_diff = point1.second - point2.second;
    return std::sqrt(x_diff * x_diff + y_diff * y_diff);
}

std::tuple<double, pair<double, double>, pair<double, double>> brute_force2(const vector<std::pair<double, double>> pointsx, int start, int end)
{

    pair<double, double> left;
    pair<double, double> right;
    double distance = 1000000000;

    for (int i = start; i < end - 1; i++)
    {
        pair<double, double> point1 = pointsx[i];
        for (int o = i + 1; o < end; o++)
        {
            pair<double, double> point2 = pointsx[o];
            double curr_dist = dist(point1, point2);
            if (curr_dist < distance)
            {
                distance = curr_dist;
                left = point1;
                right = point2;
            }
        }
    }
    return make_tuple(distance, left, right);
}
std::tuple<double, pair<double, double>, pair<double, double>> brute_force(const vector<std::pair<double, double>> pointsx, int start, int end)
{
    if (end - start == 2)
    {
        return make_tuple(dist(pointsx[start], pointsx[end - 1]), pointsx[start], pointsx[end - 1]);
    }
    return min(
        min(
            make_tuple(dist(pointsx[start], pointsx[end - 1]), pointsx[start], pointsx[end - 1]),
            make_tuple(dist(pointsx[start + 1], pointsx[end - 1]), pointsx[start + 1], pointsx[end - 1])),
        make_tuple(dist(pointsx[start], pointsx[end - 2]), pointsx[start], pointsx[end - 2]));
}
std::tuple<double, pair<double, double>, pair<double, double>> strip(const vector<std::pair<double, double>> pointsx, int start, int end, int mid, int delta)
{
    double mid_line = pointsx[mid].first;
    pair<double, double> left;
    pair<double, double> right;
    double distance = 100000000;

    for (int i = mid; i >= start; i--)
    {
        int bound = 0;
        pair<double, double> p1 = pointsx[i];
        if (abs(p1.first - mid_line) >= delta)
            break;

        for (int o = mid + 1; o < end; o++)
        {
            bound++;
            pair<double, double> p2 = pointsx[o];

            if (abs(p2.first - p1.first) >= delta or bound > 6)
                break;
            double curr_dist = dist(p1, p2);
            if (curr_dist < delta)
            {
                left = p1;
                right = p2;
                distance = curr_dist;
            }
        }
    }

    return make_tuple(distance, left, right);
}
std::tuple<double, pair<double, double>, pair<double, double>> dc(const vector<std::pair<double, double>> pointsx, int start, int end)
{
    if (end - start <= 3)
    {
        return brute_force(pointsx, start, end);
    }
    int mid = start + (end - start) / 2;
    pair<double, double> mid_point = pointsx[mid];
    tuple<double, pair<double, double>, pair<double, double>> dcl = dc(pointsx, start, mid);
    tuple<double, pair<double, double>, pair<double, double>> dcr = dc(pointsx, mid, end);
    tuple<double, pair<double, double>, pair<double, double>> sol;
    if (std::get<0>(dcl) <= std::get<0>(dcr))
    {
        sol = dcl;
    }
    else
    {
        sol = dcr;
    }
    tuple<double, pair<double, double>, pair<double, double>> strip_search = strip(pointsx, start, end, mid, std::get<0>(sol));
    if (std::get<0>(strip_search) <= std::get<0>(sol))
    {
        sol = strip_search;
    }

    return sol;
}

int main()
{
    std::string line;
    int n_points;
    double x, y;
    std::vector<std::pair<double, double>> pointsx;
    std::unordered_set<pair<double, double>> point_set;
    while (true)
    {
        pointsx.clear();
        point_set.clear();

        std::getline(std::cin, line);
        std::stringstream ss(line);
        ss >> n_points;
        if (n_points == 0)
        {
            break;
        }

        bool same = false;
        pair<double, double> same_point;
        for (int i = 0; i < n_points; i++)
        {
            std::getline(std::cin, line);
            std::stringstream ss(line);
            ss >> x >> y;
            x = round2(x);
            y = round2(y);
            pair<double, double> point = make_pair(x, y);
            if (point_set.count(point))
            {
                same = true;
                same_point = point;
            }
            pointsx.emplace_back(point);
            point_set.insert(point);
        }
        if (same)
        {
            std::cout << same_point.first << " " << same_point.second << " " << same_point.first << " " << same_point.second << "\n";
            continue;
        }
        std::sort(pointsx.begin(), pointsx.end(), [](const auto &a, const auto &b)
                  { if (a.first != b.first){
                    return a.first < b.first;
                  }
                    return a.second < b.second; });

        std::tuple<double, pair<double, double>, pair<double, double>> sol = dc(pointsx, 0, n_points);
        pair<double, double> first = std::get<1>(sol);
        pair<double, double> second = std::get<2>(sol);
        std::cout << first.first << " " << first.second << " " << second.first << " " << second.second << "\n";
    }
    return 0;
}