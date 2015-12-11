#ifndef MERGE_SORT_H
#define MERGE_SORT_H

#include <QCoreApplication>
#include "Sort_Lib.h"
#include "stdlib.h"
#include <vector>
#include <iostream>
#include <iomanip>
#include <time.h>

template<typename T> void merge_sort(std::vector<T> &list_);
template<typename T> void merge(std::vector<T>& list_, std::vector<unsigned int>& sublistptrs_);
template<typename T> void createsublists(std::vector<unsigned int>& sublistptrs_, unsigned int sublistsize_, std::vector<T> list_);

template<typename T>
void merge_sort(std::vector<T>& list_)
{
    std::vector<unsigned int> sublistptrs;
    int sublistexp = 0;
    int sublistsize = pow(2, sublistexp);
    int maxsublistexp = static_cast<int> (log2(list_.size()));

    if(!(list_.size() == 1))
    {
        for(int i = 0; i < maxsublistexp; i++)
        {
            createsublists(sublistptrs, sublistsize, list_);
            merge(list_, sublistptrs);
            sublistexp += 1;
            sublistsize = pow(2, sublistexp);
        }

    }
    return;
}

template<typename T>
void createsublists(std::vector<unsigned int>& sublistptrs_, unsigned int sublistsize_, std::vector<T> list_)
{
    sublistptrs_.resize(0);
    int sublistcount = list_.size()/sublistsize_;
    if(sublistcount%2 == 1)
    {
        sublistcount -= 1;
    }

    for(int i = 0; i < sublistcount; i++)
    {
        sublistptrs_.push_back(i * sublistsize_);
    }


    return;
}

template<typename T>
void merge(std::vector<T>& list, std::vector<unsigned int>& sublistptrs)
{
    unsigned int sublist1counter = 0, sublist2counter = 0;
    unsigned int sublist1start = 0, sublist2start = 0;
    unsigned int sublist1size = 0, sublist2size = 0;


    std::vector<T> mergedlist(0);
    std::vector<T> subsublist;

    for(unsigned int i = 0; i < sublistptrs.size()/2; i++)
    {
        sublist1counter = 0;
        sublist2counter = 0;
        sublist1start = sublistptrs[2*i];
        sublist2start = sublistptrs[2*i + 1];
        sublist1size = sublistptrs[2*i + 1] - sublistptrs[2*i];


        if(i != sublistptrs.size()/2 - 1)
        {
            sublist2size = sublistptrs[2*i + 1 + 1] - sublistptrs[2*i + 1];
        }
        else
        {
            sublist2size = list.size() - sublistptrs[2*i + 1];
            subsublist.resize(sublist2size);
            for(unsigned int j = 0; j < sublist2size; j++)
            {
                subsublist[j] = list[sublist2start + j];
            }

            merge_sort(subsublist);

            for(unsigned int j = 0; j < subsublist.size(); j++)
            {
                list[sublist2start + j] = subsublist[j];
            }

        }
        mergedlist.resize(sublist1size + sublist2size);


        while((sublist1counter < sublist1size) && (sublist2counter < sublist2size))
        {


            if(list[sublist1start + sublist1counter] < list[sublist2start + sublist2counter])  //1 < 2
            {
                mergedlist[sublist1counter + sublist2counter] = list[sublist1start + sublist1counter];
                sublist1counter++;
            }

            else if(list[sublist2start + sublist2counter] < list[sublist1start + sublist1counter]) //2 < 1
            {
                mergedlist[sublist1counter + sublist2counter] = list[sublist2start + sublist2counter];
                sublist2counter++;
            }

            else // 2 == 1
            {
                mergedlist[sublist1counter + sublist2counter] = list[sublist1start + sublist1counter];
                mergedlist[sublist1counter + sublist2counter + 1] = list[sublist2start + sublist2counter];
                sublist1counter++;
                sublist2counter++;
            }

            if(sublist1counter == sublist1size)
            {
                for(unsigned int j = 0; j < sublist2size - sublist2counter; j++)
                {
                    mergedlist[sublist1counter + sublist2counter + j] = list[sublist2start + sublist2counter + j];
                }

                sublist2counter = sublist2size;
            }

            else if(sublist2counter == sublist2size)
            {

                for(unsigned int j = 0; j < sublist1size - sublist1counter; j++)
                {
                    mergedlist[sublist2counter + sublist1counter + j] = list[sublist1start + sublist1counter + j];
                }

                sublist1counter = sublist1size;


            }
        }

        for(unsigned int k = 0; k < sublist1size + sublist2size; k++)
        {
            list[sublist1start + k] = mergedlist[k];
        }

    }

return;

}


#endif // MERGE_SORT_H
