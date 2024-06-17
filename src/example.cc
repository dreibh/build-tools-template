// Build Tool Example
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

#include "library.h"
#include "version.h"

#include <string.h>
#include <iomanip>
#include <iostream>


// ###### Main program ######################################################
int main(int argc, char** argv)
{
   // ====== Handle arguments ===============================================
   for(int i = 1; i < argc; i++) {
      if( (!(strcmp(argv[i], "-v"))) || (!(strcmp(argv[i], "--version"))) ) {
         std::cout << EXAMPLE_PACKAGE << "\n";
         return 0;
      }
      else {
         std::cerr << "Usage: " << argv[0] << " [--version|-v]\n";
         exit(1);
      }
   }

   // ====== Hello World! ===================================================
   std::cout << "This is a test!\n";

   // ====== Some ANSI color tests ==========================================
   std::cout.fill('0');
   for(unsigned int r = 0; r < 256; r += 16) {
      setColor(std::cout, r, 0, 0);
      std::cout << "Red: " << std::hex << std::uppercase << std::setw(2) << r << "\n";
      for(unsigned int g = 0; g < 256; g += 16) {
         setColor(std::cout, 0, g, 0);
         std::cout << "  Green: " << std::hex << std::uppercase << std::setw(2) << g << "\t";
         for(unsigned int b = 0; b < 256; b += 16) {
            setColor(std::cout, r, g, b);
            std::cout << "|" << std::hex << std::uppercase
                      << std::setw(2) << r << std::setw(2) << g << std::setw(2) << b
                      << std::dec;
         }
         std::cout << "|\n";
         resetColor(std::cout);
      }
      std::cout << "\n";
   }

   return 0;
}
