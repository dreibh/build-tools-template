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



// ###### Main program ######################################################
int main(int argc, char** argv)
{
   std::cout << "This is a test!\n";

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
