# CMake-CPP-setup

This repo is as  a guide for someone who wants to learn CMake, Conan, and some other tools usage for their CPP code. WSL in VS Code is used in this project.

## Steps

0 Create source and CMakeFile
1 mkdir build
2 cd build
3 cmake .. - Generate the build files (Makefile) / Configure the project
4 cmake --build . //we are in build directory so --build and . is relative path
5 ./Executable
6 cmake (options) -S (path-to-source) -B (path-to-build) eg: when we are in build directory cmake -S .. -B . or in short just cmake .. 7 cmake --help shows all generators 8 -G to explicitly use a particular build system generator.
9 To build only the static library: cmake --build . --target Library
10 If you have a subdirectory with source file, then always make a sub CMakefile for the directory.
11 If you want to go multiple level down in a directory have directory under directory, just add CMakeLists.txt to all subdirectories even
if they dont have any code files in those subdirectories , add -> add_subdirectory("subdirectory_name_here")
