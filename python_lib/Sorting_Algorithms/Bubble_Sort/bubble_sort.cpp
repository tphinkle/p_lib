#include "../Sort_Lib/Sort_Lib.h"
#include <vector>
/////////////////////////////////
///
/// Bubble sort: O(n^2)
///
/// Loops through a list element
/// by element, switching elements
/// in a pair if they are out of
/// order
///
//////////////////////////////////

template <typename T>
void bubble_sort(std::vector<T>& list)
{
    bool sorted = false;
    int exchanges;
    T tempholder;
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

