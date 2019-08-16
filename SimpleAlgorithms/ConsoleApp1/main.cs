using System;

namespace SimpleAlgorithms
{
    public class main
    {
        static public void Main(string[] args)
        {
            int[] arr = new int[] { 6, 7, 2, 44, 6, 5 };
            Console.WriteLine(string.Join(",", arr));
            Rotate.RotateN(arr, 2);
            Console.WriteLine(string.Join(",", arr));
            Console.ReadLine();

        }
    }
}