cmake_minimum_required(VERSION 3.22)


project(
    CppProjectTemplate 
    VERSION 1.0.0 
    LANGUAGES CXX)

set(LIBRARY_NAME Library)

#Tell CMake where to search for sub CMake files.
add_subdirectory(src) # src must be defined first, because we are using the library in app.
add_subdirectory(inc) # inc comes after src, need to keep this order.
add_subdirectory(app)



