using System;
namespace SimpleAlgorithms
{
    public class Naturals
    {
        public static int sumNaturals(int n)
        //Algebraic way of finding the sum of the first n natural numbers
        {
            if (n > 0)
            {
                return n * (n + 1) / 2;
            }
            else throw new ArgumentOutOfRangeException("n", "Number must be a natural number");
        }
    }
}
