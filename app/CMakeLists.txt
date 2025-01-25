add_executable(Executable main.cc)
target_link_libraries(Executable PUBLIC Library) # We are linking our library to our executable, so when we build our executable, library gets built with it