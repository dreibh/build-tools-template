# Build Tools Template
# Copyright (C) 2024-2026 by Thomas Dreibholz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact: thomas.dreibholz@gmail.com

CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
PROJECT(td-build-tools-template)
ENABLE_LANGUAGE(CXX)

SET(BUILD_MAJOR "0")
SET(BUILD_MINOR "1")
SET(BUILD_PATCH "0")
SET(BUILD_VERSION ${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH})


#############################################################################
#### INSTALLATION_DIRECTORIES                                            ####
#############################################################################

# See: https://cmake.org/cmake/help/v3.0/module/GNUInstallDirs.html
INCLUDE(GNUInstallDirs)


#############################################################################
#### PACKAGING                                                           ####
#############################################################################

SET(CPACK_SOURCE_GENERATOR "TXZ")
SET(CPACK_SOURCE_PACKAGE_FILE_NAME
    "${CMAKE_PROJECT_NAME}-${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}")
SET(CPACK_SOURCE_IGNORE_FILES "\\\\.git;\\\\.swp$;~$;\\\\.\\\\#;/\\\\#")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "^${PROJECT_SOURCE_DIR}/${CMAKE_PROJECT_NAME}[_-]")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "\\\\.cmake$|\\\\.make$|\\\\.log$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/CMakeCache\\\\.txt$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/(CMakeFiles|CMakeScripts|_CPack_Packages)/")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/package-version\\\\.h$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/packaging\\\\.conf$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "^${PROJECT_SOURCE_DIR}/(po.*/|src.*/|)Makefile$")
INCLUDE(CPack)

ADD_CUSTOM_TARGET(dist COMMAND ${CMAKE_MAKE_PROGRAM} clean package_source)


#############################################################################
#### UNINSTALL                                                           ####
#############################################################################

IF(NOT TARGET uninstall)
   CONFIGURE_FILE(
      "${CMAKE_CURRENT_SOURCE_DIR}/cmake_uninstall.cmake.in"
      "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
      IMMEDIATE @ONLY)

   ADD_CUSTOM_TARGET(uninstall
      COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake)
ENDIF()


#############################################################################
#### OS DEPENDENT                                                        ####
#############################################################################

IF (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
   MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "FreeBSD")
   MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
   SET(CMAKE_REQUIRED_INCLUDES "/usr/local/include" "/usr/include")
   SET(CMAKE_LIBRARY_PATH "/usr/local/lib")
   INCLUDE_DIRECTORIES("/usr/local/include")

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
   MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
   SET(CMAKE_REQUIRED_INCLUDES "/usr/local/include" "/usr/include" "/usr/local/opt/openssl/include")
   SET(CMAKE_LIBRARY_PATH "/usr/local/lib")
   INCLUDE_DIRECTORIES("/usr/local/include" "/usr/local/opt/openssl/include")

ELSEIF (${CMAKE_SYSTEM_NAME} MATCHES "NetBSD")
   MESSAGE(STATUS ${CMAKE_SYSTEM_NAME} " supported")
   SET(CMAKE_REQUIRED_INCLUDES "/usr/pkg/include" "/usr/include" "/usr/local/include")
   SET(CMAKE_LIBRARY_PATH "/usr/local/lib")
   INCLUDE_DIRECTORIES("/usr/pkg/include" "/usr/local/include")

ELSE()
   MESSAGE(FATAL_ERROR ${CMAKE_SYSTEM_NAME} " not supported (yet?)")

ENDIF()


#############################################################################
#### INTERNATIONALISATION (I18N)                                         ####
#############################################################################

FIND_PACKAGE (Intl)
IF (Intl_FOUND)
   MESSAGE(STATUS "Internationalization (i18n) found:")
   MESSAGE(STATUS " INTL_INCLUDE_DIRS: ${Intl_INCLUDE_DIRS}")
   MESSAGE(STATUS " INTL_LIBRARIES: ${Intl_LIBRARIES}")
   MESSAGE(STATUS " Version: ${Intl_VERSION}")
   INCLUDE_DIRECTORIES(${Intl_INCLUDE_DIRS})
   LINK_DIRECTORIES(${Intl_LIBRARY_DIRS})
ELSE()
   MESSAGE(STATUS "Internationalization (i18n) not found!")
ENDIF()

FIND_PROGRAM(XGETTEXT xgettext REQUIRED)
FIND_PROGRAM(MSGMERGE msgmerge REQUIRED)
FIND_PROGRAM(MSGFMT   msgfmt   REQUIRED)


#############################################################################
#### OPTIONS                                                             ####
#############################################################################

OPTION(WITH_STATIC_LIBRARIES "Build static libraries" 0)
OPTION(WITH_SHARED_LIBRARIES "Build shared libraries" 1)
IF ((NOT WITH_STATIC_LIBRARIES) AND (NOT WITH_SHARED_LIBRARIES))
   MESSAGE(FATAL_ERROR "Static (WITH_STATIC_LIBRARIES) or shared (WITH_SHARED_LIBRARIES) libraries must be enabled!")
ENDIF()

OPTION(STATIC_BUILD "Build statically-linked executables" 0)
IF (STATIC_BUILD)
   IF (WITH_SHARED_LIBRARIES)
      MESSAGE(FATAL_ERROR "STATIC_BUILD=ON cannot be used with WITH_SHARED_LIBRARIES=ON!")
   ENDIF()
   MESSAGE("Building static executables")
   SET(CMAKE_FIND_LIBRARY_SUFFIXES ".a")
   SET(Boost_USE_STATIC_LIBS ON)
   SET(CMAKE_EXE_LINKER_FLAGS "-static")
ELSE()
   IF (NOT WITH_SHARED_LIBRARIES)
      MESSAGE(FATAL_ERROR "STATIC_BUILD=OFF cannot be used with WITH_SHARED_LIBRARIES=OFF!")
   ENDIF()
ENDIF()


#############################################################################
#### SUBDIRECTORIES                                                      ####
#############################################################################

ADD_SUBDIRECTORY(po)
ADD_SUBDIRECTORY(src)
