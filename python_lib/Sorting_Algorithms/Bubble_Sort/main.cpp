#include <QCoreApplication>
#include "bubble_sort.h"
#include "../Sort_Lib/Sort_Lib.h"
#include "stdlib.h"
#include <vector>
#include <iostream>
#include <iomanip>
#include <time.h>

int main(int argc, char *argv[])
{
    time_t t1, t2, t3;

    std::vector<int> list(100);

    t1 = time(NULL);

    populate_list(list);

    t2 = time(NULL);

    bubble_sort(list);



    t3 = time(NULL);

    std::cerr << "populate time: " << t2 - t1 << "\nsort time: " << t3 - t2 << "\n";

    return 0;
}
