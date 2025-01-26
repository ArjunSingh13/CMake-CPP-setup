cmake_minimum_required(VERSION 3.22)


project(
    CppProjectTemplate 
    VERSION 1.0.0 
    LANGUAGES CXX)

set(CMAKE_CXX_STANDARD          17) # Setup what standard you want to use.
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS        OFF)  #gcc and g++ has some extra features that are not part of standard c and c++, so we disable those features.


set(LIBRARY_NAME "Library") # create a cmake variable, use in all subdirectories.
set(EXECUTABLE_NAME "Executable")

option(COMPILE_EXECUTABLE "Whether to compile the executable" ON) #adding option to choose between if main app should be built as exec or not.

#Tell CMake where to search for sub CMake files.
add_subdirectory(configured)
add_subdirectory(src) # src must be defined first, because we are using the library in app.
add_subdirectory(inc) # inc comes after src, need to keep this order.

if(COMPILE_EXECUTABLE)
    add_subdirectory(app)
else()
    message("Compiling without executable")
endif()


