// Build Tool Template Example Program
// Copyright (C) 2024 by Thomas Dreibholz
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// Contact: thomas.dreibholz@gmail.com

#include "package-version.h"

#include <libintl.h>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// ###### Main program ######################################################
int main(int argc, char** argv)
{
   // ====== Initialise i18n support ========================================
   if(setlocale(LC_ALL, "") == NULL) {
      setlocale(LC_ALL, "C.UTF-8");   // "C" should exist on all systems!
   }
   bindtextdomain("example-program1", NULL);
   textdomain("example-program1");

   // ====== Handle arguments ===============================================
   for(int i = 1; i < argc; i++) {
      if( (!(strcmp(argv[i], "-v"))) || (!(strcmp(argv[i], "--version"))) ) {
         puts(EXAMPLE_PACKAGE);
         return 0;
      }
      else {
         fprintf(stderr, "%s %s [--version|-v]\n", gettext("Usage:"), argv[0]);
         exit(1);
      }
   }

   // ====== Hello World! ===================================================
   printf("%s\n", gettext("This is a test!"));

   return 0;
}
