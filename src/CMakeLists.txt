# Build Tools Template
# Copyright (C) 2024 by Thomas Dreibholz
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

#############################################################################
#### VERSION FILE                                                        ####
#############################################################################

CONFIGURE_FILE (
   "${CMAKE_CURRENT_SOURCE_DIR}/package-version.h.in"
   "${CMAKE_CURRENT_BINARY_DIR}/package-version.h"
)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR})


#############################################################################
#### LIBRARIES                                                           ####
#############################################################################

# ====== libexamplelibrary =========================================================
LIST(APPEND libexamplelibrary_headers
   example-library.h
)
LIST(APPEND libexamplelibrary_sources
   example-library.cc
)

INSTALL(FILES ${libexamplelibrary_headers} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/example)

IF (WITH_STATIC_LIBRARIES)
   ADD_LIBRARY(libexamplelibrary-static STATIC ${libexamplelibrary_sources})
ENDIF()
IF (WITH_SHARED_LIBRARIES)
   ADD_LIBRARY(libexamplelibrary-shared SHARED ${libexamplelibrary_sources})
ENDIF()
FOREACH(TYPE shared;static)
   IF ( (("${TYPE}" STREQUAL "static") AND (WITH_STATIC_LIBRARIES)) OR
        (("${TYPE}" STREQUAL "shared") AND (WITH_SHARED_LIBRARIES)) )
      SET_TARGET_PROPERTIES(libexamplelibrary-${TYPE} PROPERTIES
         OUTPUT_NAME examplelibrary
         VERSION     ${BUILD_VERSION}
         SOVERSION   ${BUILD_MAJOR})
      # TARGET_LINK_LIBRARIES (libexamplelibrary-${TYPE} ...)
      INSTALL(TARGETS libexamplelibrary-${TYPE} DESTINATION ${CMAKE_INSTALL_LIBDIR})
   ENDIF()
ENDFOREACH()


#############################################################################
#### PROGRAMS                                                            ####
#############################################################################

IF (STATIC_BUILD)
   SET(libraryType static)
ELSE()
   SET(libraryType shared)
ENDIF()

# ====== Example Program 1 ==================================================
ADD_EXECUTABLE(example-program1 example-program1.c)
TARGET_LINK_LIBRARIES(example-program1 ${Intl_LIBRARIES})
INSTALL(TARGETS     example-program1   RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES       example-program1.1 DESTINATION         ${CMAKE_INSTALL_MANDIR}/man1)
INSTALL(FILES       example-program1.bash-completion
        DESTINATION ${CMAKE_INSTALL_DATADIR}/bash-completion/completions
        RENAME      example-program1)

# ====== Example Program 2 ==================================================
ADD_EXECUTABLE(example-program2 example-program2.cc)
TARGET_LINK_LIBRARIES(example-program2 libexamplelibrary-${libraryType} ${Intl_LIBRARIES})
INSTALL(TARGETS     example-program2   RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES       example-program2.1 DESTINATION         ${CMAKE_INSTALL_MANDIR}/man1)
INSTALL(FILES       example-program2.bash-completion
        DESTINATION ${CMAKE_INSTALL_DATADIR}/bash-completion/completions
        RENAME      example-program2)

# ====== Example Script 1 ===================================================
INSTALL(PROGRAMS example-script1 DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES example-script1.1  DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)

# ====== Example Script 2 ===================================================
INSTALL(PROGRAMS example-script2 DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES example-script2.1  DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)


#############################################################################
#### EXAMPLES                                                            ####
#############################################################################

INSTALL(FILES
           example-file1.txt
           example-file2.jpeg
        DESTINATION ${CMAKE_INSTALL_DATADIR}/doc/build-tools-template/examples)
