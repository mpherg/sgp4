cmake_minimum_required(VERSION 2.8.6)
project(sgp4)

# Call the conanbuildinfo.cmake file, if it exists
if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  conan_basic_setup()
endif()

add_subdirectory(src)
