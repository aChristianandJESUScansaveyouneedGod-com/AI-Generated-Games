cmake_minimum_required(VERSION 3.10)

project(AIGeneratedGame)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set output directory
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/Release)

# Add executable
add_executable(AIGeneratedGame
    Game/main.cpp
)

# Optional future folders
include_directories(
    Engine
)
