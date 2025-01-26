#configure file function is telling source file and then destination file. CMake pickup the source file, modify data and store at destination location.
#below CMAKE_BINARY_DIR is the path to build, its a default inbuilt variable of cmake.
# We added ESCAPE_QUOTES so cmake can handle all content correctly.
configure_file(
    "config.hpp.in"
    "${CMAKE_BINARY_DIR}/configured_files/include/config.hpp" ESCAPE_QUOTES
)