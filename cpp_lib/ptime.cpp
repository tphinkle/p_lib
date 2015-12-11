#include <ctime>

#include "ptime.h"

void pWait(int seconds)
{
    clock_t temp;
    temp = clock() + seconds * CLOCKS_PER_SEC ;
    while (clock() < temp)
    {}

    return;
}
