using System;

namespace SimpleAlgorithms
{
    public class GradeLiterals
    {
        public static char GradeLiteral(int x)
        //Returns numeric grades in literals according to the following scheme: 0-40=D, 40-50=C, 50-60=B, 60-75=A, 75-100=S
        {
            if (x >= 0 && x <= 100)
            {
                if (x <= 40)
                    return 'D';
                else if (x <= 50 && x > 40)
                    return 'C';
                else if (x <= 60 && x > 50)
                    return 'B';
                else if (x <= 75 && x > 60)
                    return 'A';
                else
                    return 'S';
            }
            throw new ArgumentOutOfRangeException("x", "Grade must be between 0 and 100.");
        }
    }
}