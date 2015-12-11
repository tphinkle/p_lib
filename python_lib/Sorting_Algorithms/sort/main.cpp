#include <QCoreApplication>
#include "../Sort_Lib/bubble_sort.h"
#include "../Sort_Lib/Merge_Sort.h"
#include "../Sort_Lib/Sort_Lib.h"

int main(int argc, char *argv[])
{
    int bubblestart, bubbleend, bubbleduration;
    int mergestart, mergeend, mergeduration;


    std::vector<double> list1(300000);
    std::vector<double> list2(300000);

    populate_list(list1);

    list2 = copy_list(list1);

    bubblestart = time(NULL);
    bubble_sort(list1);
    bubbleend = time(NULL);

    mergestart = time(NULL);
    merge_sort(list1);
    mergeend = time(NULL);

    bubbleduration = bubbleend - bubblestart;
    mergeduration = mergeend - mergestart;

    std::cerr << "bubble duration = " << bubbleduration << "\nmerge duration = " << mergeduration << "\n";

    return 0;
}
