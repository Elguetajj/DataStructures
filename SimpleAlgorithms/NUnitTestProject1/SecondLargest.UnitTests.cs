using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using NUnit.Framework;
using SimpleAlgorithms;

namespace SImpleAlgorithmsTests
{
    [TestFixture]
    class SecondLargestUnitTests
    {
        [Test, TestCaseSource(typeof(SecondLargestDataProvider),"SecondLargestTestCases")]
        public int SecondLargestTest(int[] ar)
        {
            return SecondLargest.secondLargest(ar);
        }
    }

    public class SecondLargestDataProvider
    {
        public static IEnumerable SecondLargestTestCases
        {
            get
            {
                yield return new TestCaseData(new int[] { 1, 2, 3, 4, 5, 6 }).Returns(5);
                yield return new TestCaseData(new int[] { -2, -1, 0, 1, 2, 3 }).Returns(2);
                yield return new TestCaseData(new int[] { 88, 15, 66, 8, 9, 100 }).Returns(88);
            }
        }
    }
}
