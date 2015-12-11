#ifndef BUBBLE_SORT_H
#define BUBBLE_SORT_H

#include <vector>
#include "Sort_Lib.h"


template<typename T> void bubble_sort(std::vector<T>& list);

template <typename T>
void bubble_sort(std::vector<T>& list)
{
    bool sorted = false;
    int exchanges;

    while(sorted == false)
    {
        exchanges = 0;
        for(int i = 0; i < list.size() - 1; i++)
        {
            if(list[i] > list[i + 1])
            {
                switch_values(list[i], list[i+1]);
                exchanges += 1;
            }
        }
        if (exchanges == 0)
        {
            sorted = true;
        }
    }

    return;
}


#endif // BUBBLE_SORT_H
