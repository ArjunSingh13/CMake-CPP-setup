set(EXE_SOURCES
    "main.cc")

add_executable(${EXECUTABLE_NAME} ${EXE_SOURCES})

# Include the configured directory
target_include_directories(${EXECUTABLE_NAME} PUBLIC "${CMAKE_BINARY_DIR}/configured_files/include")

target_link_libraries(${EXECUTABLE_NAME} PUBLIC ${LIBRARY_NAME} ) # We are linking our library to our executable, so when we build our executable, library gets built with it