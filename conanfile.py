from conans import ConanFile, CMake, tools
import os


class Sgp4Conan(ConanFile):
    name = "sgp4"
    version = "2011-12-30"
    license = "MIT"
    url = "https://github.com/mpherg/sgp4"
    settings = "os", "compiler", "build_type", "arch"
    options = {
            "shared": [True, False],
            "fpic": [True, False]
            }
    default_options = (
            "shared=False",
            "fpic=True"
            )
    generators = "cmake"
    src_dir = "."

    def source(self):
        self.run("git clone https://github.com/mpherg/sgp4.git")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON" if self.options.shared else "OFF"
        cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON" if self.options.fpic else "OFF"
        cmake.definitions["CONAN_SYSTEM_INCLUDES"] = "ON"
        if os.path.exists(self.source_folder + "/sgp4/conanfile.py"):
            self.src_dir = self.source_folder + "/sgp4"
        cmake.configure(source_dir=self.src_dir, build_dir=".")
        cmake.build()

    def package(self):
        self.copy("sgp4unit.h", dst="include", src=self.src_dir + "/src")
        self.copy("sgp4io.h", dst="include", src=self.src_dir + "/src")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [self.name]
