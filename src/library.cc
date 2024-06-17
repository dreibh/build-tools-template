#include <iomanip>
#include <iostream>


// ###### Set ANSI color in terminal ########################################
void setColor(std::ostream& os, unsigned int r, unsigned int g, unsigned int b)
{
   os << "\x1b[38;2;" << std::dec
      << r << ";" << g << ";" << b << "m";
}


// ###### Reset ANSI color in terminal ######################################
void resetColor(std::ostream& os)
{
    os << "\x1b[0m";
}
