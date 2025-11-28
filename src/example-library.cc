// Build Tool Example
// Copyright (C) 2024-2025 by Thomas Dreibholz
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

#include <stdlib.h>

#include <iomanip>
#include <iostream>


// ###### Set ANSI color in terminal ########################################
void setColor(std::ostream& os, unsigned int r, unsigned int g, unsigned int b)
{
   os << "\e[38;2;" << std::dec
      << r << ";" << g << ";" << b << "m";
}


// ###### Reset ANSI color in terminal ######################################
void resetColor(std::ostream& os)
{
    os << "\e[0m";
}


// ###### Reset ANSI color in terminal ######################################
void abortWithError(const char* message)
{
   std::cerr << message << "\n";
   abort();
}
