# This way we can add as many files as we need in this variable and just use variable name.
set(LIBRARY_SOURCES
    "my_lib.cc")

#set(LIBRARY_HEADERS
#   "my_lib.h")

add_library(${LIBRARY_NAME} STATIC 
        ${LIBRARY_SOURCES})


target_include_directories(${LIBRARY_NAME} PUBLIC "./"  
                                                  "../inc"
                                                   ) # to tell CMake where are the header files for this library.
