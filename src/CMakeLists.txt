include_directories(${CMAKE_CURRENT_LIST_DIR})

set(src
    sgp4ext.cpp
    sgp4io.cpp
    sgp4unit.cpp)

add_library(sgp4 ${src})

install(FILES       sgp4io.h sgp4unit.h
        DESTINATION usr/local/include)
install(TARGETS     sgp4 sgp4
        DESTINATION usr/local/lib)
