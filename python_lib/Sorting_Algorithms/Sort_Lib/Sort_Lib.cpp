#include <vector>
#include <random>
#include <iomanip>
#include <iostream>

template <typename T>
void switch_values(T& t1, T& t2)
{
    T tempvalue;
    tempvalue = t1;
    t1 = t2;
    t2 = tempvalue;

    return;
}

template <typename T>
void populate_list(std::vector<T>& list)
{
    srand(time(NULL));
    for(int i = 0; i < list.size(); i++)
    {
        list[i] = rand()*1.0*list.size()/RAND_MAX;
    }

    return;
}

template <typename T>
void print_list(std::vector<T>& list)
{
    for(int i = 0; i < list.size(); i++ )
    {
        std::cerr << list[i] << " ";
    }

    return;
}

