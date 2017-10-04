project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(testsgp4 test.cpp)
target_link_libraries(testsgp4 ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
enable_testing()
add_test(NAME testsgp4
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND testsgp4)
