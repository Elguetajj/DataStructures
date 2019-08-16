namespace SimpleAlgorithms
{
    public class Rotate
    {
        public static void Reverse(int[] arr, int first, int last)
        {
            int temp;
            for (int i = first, j = last; i < j; i++, j--)
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        public static void RotateN(int[] arr, int n)
        {
            Reverse(arr, arr.Length - n, arr.Length-1);
            Reverse(arr, 0, arr.Length-1 - n);
            Reverse(arr, 0, arr.Length - 1);
        }
    }
}