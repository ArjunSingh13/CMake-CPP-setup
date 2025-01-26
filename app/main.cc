#include <iostream>
#include "my_lib.h"

// because we also did add_subdirectory(configured) in top level CMakeLists.txt, 
// so we can included this file even if its in build folder.
#include "config.hpp" 

int main()
{
    std::cout << "Hello World\n";
    std::cout << project_name << '\n'; // these variables values are coming from build folder, but they get updated when we make change in CMakeLists.txt
    std::cout << project_version << '\n';

    return 0;
}