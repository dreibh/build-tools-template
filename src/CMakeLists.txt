#  =================================================================
#           #     #                 #     #
#           ##    #   ####   #####  ##    #  ######   #####
#           # #   #  #    #  #    # # #   #  #          #
#           #  #  #  #    #  #    # #  #  #  #####      #
#           #   # #  #    #  #####  #   # #  #          #
#           #    ##  #    #  #   #  #    ##  #          #
#           #     #   ####   #    # #     #  ######     #
#
#        ---   The NorNet Testbed for Multi-Homed Systems  ---
#                        https://www.nntb.no
#  =================================================================
#
#  High-Performance Connectivity Tracer (HiPerConTracer)
#  Copyright (C) 2015-2024 by Thomas Dreibholz
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  Contact: dreibh@simula.no

#############################################################################
#### VERSION FILE                                                        ####
#############################################################################

CONFIGURE_FILE (
   "${CMAKE_CURRENT_SOURCE_DIR}/version.h.in"
   "${CMAKE_CURRENT_SOURCE_DIR}/version.h"
)


#############################################################################
#### LIBRARIES                                                           ####
#############################################################################

# ====== liblibrary =========================================================
LIST(APPEND liblibrary_headers
   library.h
)
LIST(APPEND liblibrary_sources
   library.cc
)

INSTALL(FILES ${liblibrary_headers} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/example)

IF (WITH_STATIC_LIBRARIES)
   ADD_LIBRARY(liblibrary-static STATIC ${liblibrary_sources})
ENDIF()
IF (WITH_SHARED_LIBRARIES)
   ADD_LIBRARY(liblibrary-shared SHARED ${liblibrary_sources})
ENDIF()
FOREACH(TYPE shared;static)
   IF ( (("${TYPE}" STREQUAL "static") AND (WITH_STATIC_LIBRARIES)) OR
        (("${TYPE}" STREQUAL "shared") AND (WITH_SHARED_LIBRARIES)) )
      SET_TARGET_PROPERTIES(liblibrary-${TYPE} PROPERTIES OUTPUT_NAME example CLEAN_DIRECT_OUTPUT 1)
      SET_TARGET_PROPERTIES(liblibrary-${TYPE} PROPERTIES
         VERSION   ${BUILD_VERSION}
         SOVERSION ${BUILD_MAJOR}
      )
      TARGET_LINK_LIBRARIES (liblibrary-${TYPE} ${Boost_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT} ${LZMA_LIBRARY} ${BZ2_LIBRARY} ${Z_LIBRARY})
      INSTALL(TARGETS liblibrary-${TYPE} DESTINATION ${CMAKE_INSTALL_LIBDIR})
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

# ====== Example ============================================================
ADD_EXECUTABLE(example example.cc)
TARGET_LINK_LIBRARIES(example liblibrary-${libraryType})
INSTALL(TARGETS example RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES example.1 DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)


#############################################################################
#### EXAMPLES                                                            ####
#############################################################################

INSTALL(FILES example.txt
        DESTINATION ${CMAKE_INSTALL_DATADIR}/doc/example/examples)
