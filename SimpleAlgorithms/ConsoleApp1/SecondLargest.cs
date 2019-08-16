namespace SimpleAlgorithms
{
    public class SecondLargest
    {
        public static int secondLargest(int[] arr)
        {
            int largest=0;
            int secondLargest = 0;
            foreach (var i in arr)
            {
                if (i > largest)
                {
                    secondLargest = largest;
                    largest = i;
                }
            }
            return secondLargest;
        }
    }
}