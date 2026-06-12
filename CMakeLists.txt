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
SET(BUILD_PATCH "3")
SET(BUILD_VERSION ${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH})


#############################################################################
#### CMAKE INCLUDES                                                      ####
#############################################################################

INCLUDE(CheckCCompilerFlag)
INCLUDE(CheckCSourceCompiles)
INCLUDE(CheckCSourceRuns)
INCLUDE(CheckIncludeFile)
INCLUDE(CheckStructHasMember)
INCLUDE(GNUInstallDirs)


#############################################################################
#### PACKAGING                                                           ####
#############################################################################

SET(CPACK_SOURCE_GENERATOR "TXZ")
SET(CPACK_SOURCE_PACKAGE_FILE_NAME
    "${CMAKE_PROJECT_NAME}-${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}")
SET(CPACK_SOURCE_IGNORE_FILES "\\\\.git;\\\\.swp$;~$;\\\\.\\\\#;/\\\\#")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "^${PROJECT_SOURCE_DIR}/${CMAKE_PROJECT_NAME}[_-]")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "\\\\.make$|\\\\.log$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/CMakeCache\\\\.txt$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/(CMakeFiles|CMakeScripts|_CPack_Packages)/")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/package-version\\\\.h$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "/packaging\\\\.conf$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "^${PROJECT_SOURCE_DIR}/(po.*/|src.*/|)Makefile$")
LIST(APPEND CPACK_SOURCE_IGNORE_FILES "^${PROJECT_SOURCE_DIR}/(po.*|src.*|[^/]*)\\\\.cmake$")
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

IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
   MESSAGE(STATUS "${CMAKE_SYSTEM_NAME} supported")
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
   MESSAGE(STATUS "${CMAKE_SYSTEM_NAME} supported")
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "NetBSD")
   MESSAGE(STATUS "${CMAKE_SYSTEM_NAME} supported")
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "OpenBSD")
   MESSAGE(STATUS "${CMAKE_SYSTEM_NAME} supported")
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Darwin")
   MESSAGE(STATUS "${CMAKE_SYSTEM_NAME} supported")
ELSE()
   MESSAGE(FATAL_ERROR "${CMAKE_SYSTEM_NAME} not supported (yet?)")
ENDIF()


#############################################################################
#### OPTIONS                                                             ####
#############################################################################

OPTION(WITH_I18N             "Build with Internationalization (i18n) support" ON)

OPTION(WITH_STATIC_LIBRARIES "Build static libraries"                         OFF)
OPTION(WITH_SHARED_LIBRARIES "Build shared libraries"                         ON)
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
#### INTERNATIONALISATION (I18N)                                         ####
#############################################################################

IF (WITH_I18N)
   FIND_PACKAGE(Intl)
   IF (Intl_FOUND)
      MESSAGE(STATUS "Internationalization (i18n) support found:")
      MESSAGE(STATUS " Intl_INCLUDE_DIRS: ${Intl_INCLUDE_DIRS}")
      MESSAGE(STATUS " Intl_LIBRARIES:    ${Intl_LIBRARIES}")
      MESSAGE(STATUS " Version:           ${Intl_VERSION}")
   ELSE()
      MESSAGE(FATAL_ERROR
            "Cannot find Internationalization (i18n) support! Try:\n"
            " * Ubuntu/Debian: sudo apt install -y libc6-dev\n"
            " * Fedora:        sudo dnf install -y gettext-devel\n"
            " * SuSE:          sudo zypper install -y gettext-devel\n"
            " * Alpine:        sudo apk add gettext-dev\n"
            " * FreeBSD:       sudo pkg install -y gettext\n"
            " * NetBSD:        sudo pkgin -y install gettext\n"
            " * OpenBSD:       sudo pkg_add gettext-runtime gettext-tools\n"
            " * Apple:         brew install gettext")
   ENDIF()

   FIND_PROGRAM(XGETTEXT xgettext HINTS /usr/pkg/bin /opt/homebrew/opt/gettext/bin /usr/local/opt/gettext/bin)
   FIND_PROGRAM(MSGMERGE msgmerge HINTS /usr/pkg/bin /opt/homebrew/opt/gettext/bin /usr/local/opt/gettext/bin)
   FIND_PROGRAM(MSGFMT   msgfmt   HINTS /usr/pkg/bin /opt/homebrew/opt/gettext/bin /usr/local/opt/gettext/bin)

   IF (XGETTEXT AND MSGMERGE AND MSGFMT)
      MESSAGE(STATUS "GNU gettext support found:")

      EXECUTE_PROCESS(COMMAND ${XGETTEXT} --version
                      OUTPUT_VARIABLE XGETTEXT_OUTPUT
                      ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)
      STRING(REGEX MATCH "([0-9]+\\.[0-9]+\\.[0-9]+|[0-9]+\\.[0-9]+)" XGETTEXT_VERSION "${XGETTEXT_OUTPUT}")

      EXECUTE_PROCESS(COMMAND ${MSGMERGE} --version
                      OUTPUT_VARIABLE MSGMERGE_OUTPUT
                      ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)
      STRING(REGEX MATCH "([0-9]+\\.[0-9]+\\.[0-9]+|[0-9]+\\.[0-9]+)" MSGMERGE_VERSION "${MSGMERGE_OUTPUT}")

      EXECUTE_PROCESS(COMMAND ${MSGFMT} --version
                      OUTPUT_VARIABLE MSGFMT_OUTPUT
                      ERROR_QUIET OUTPUT_STRIP_TRAILING_WHITESPACE)
      STRING(REGEX MATCH "([0-9]+\\.[0-9]+\\.[0-9]+|[0-9]+\\.[0-9]+)" MSGFMT_VERSION "${MSGFMT_OUTPUT}")

      MESSAGE(STATUS " xgettext: ${XGETTEXT} (version ${XGETTEXT_VERSION})")
      MESSAGE(STATUS " msgmerge: ${MSGMERGE} (version ${MSGMERGE_VERSION})")
      MESSAGE(STATUS " msgfmt:   ${MSGFMT} (version ${MSGFMT_VERSION})")
   ENDIF()

   SET(GETTEXT_MIN_VERSION 0.19)
   IF ((NOT XGETTEXT) OR (NOT MSGMERGE) OR (NOT MSGFMT)       OR
       (XGETTEXT_VERSION VERSION_LESS ${GETTEXT_MIN_VERSION}) OR
       (MSGMERGE_VERSION VERSION_LESS ${GETTEXT_MIN_VERSION}) OR
       (MSGFMT_VERSION   VERSION_LESS ${GETTEXT_MIN_VERSION}))
      MESSAGE(FATAL_ERROR
              "Cannot find gettext tools >= ${GETTEXT_MIN_VERSION}! Try:\n"
              " * Ubuntu/Debian: sudo apt install -y gettext\n"
              " * Fedora:        sudo dnf install -y gettext\n"
              " * SuSE:          sudo zypper install -y gettext\n"
              " * Alpine:        sudo apk add gettext-dev\n"
              " * FreeBSD:       sudo pkg install -y gettext-tools\n"
              " * NetBSD:        sudo pkgin -y install gettext-tools\n"
              " * OpenBSD:       sudo pkg_add gettext-tools\n"
              " * Apple:         brew install gettext")
   ENDIF()

   ADD_DEFINITIONS(-DENABLE_NLS)
ENDIF()


#############################################################################
#### SUBDIRECTORIES                                                      ####
#############################################################################

ADD_SUBDIRECTORY(po)
ADD_SUBDIRECTORY(src)
