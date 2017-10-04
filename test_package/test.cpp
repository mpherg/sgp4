#include <sgp4io.h>
#include <sgp4unit.h>
#include <iostream>
using namespace std;

int main()
{
  char line1[130] =
      "1 19822U 89016A   17277.24004501  .00032145  25768-6  61862-3 0  9991";
  char line2[130] =
      "2 19822  75.0359 165.3366 1887054  21.6922 345.4271 11.73897137922015";

  elsetrec satrec;
  double startmfe;
  double stopmfe;
  double deltamin;
  twoline2rv(line1, line2, 'c', 'e', 'a', wgs84, startmfe, stopmfe, deltamin,
             satrec);

  return 0;
}
