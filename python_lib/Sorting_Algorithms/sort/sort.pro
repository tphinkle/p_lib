#-------------------------------------------------
#
# Project created by QtCreator 2015-05-19T19:29:32
#
#-------------------------------------------------

QT       += core

QT       -= gui

TARGET = sort
CONFIG   += console
CONFIG   -= app_bundle
CONFIG   += c++11

TEMPLATE = app


SOURCES += main.cpp \
    ../Sort_Lib/Sort_Lib.cpp

HEADERS += \
    ../Sort_Lib/bubble_sort.h \
    ../Sort_Lib/Merge_Sort.h \
    ../Sort_Lib/Sort_Lib.h
