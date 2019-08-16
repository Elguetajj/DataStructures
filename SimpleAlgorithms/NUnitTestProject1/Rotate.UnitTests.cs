using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using NUnit.Framework;
using SimpleAlgorithms;

namespace SImpleAlgorithmsTests
{
    [TestFixture]
    class RotateUnitTests
    {
        [Test,TestCaseSource(typeof(RotateDataProvider),"RotateTestCases")]
        public void RotateTest(int [] arr, int n, int[]expected)
        {
            Rotate.RotateN(arr, n);
            Assert.AreEqual(expected, arr);
        }


    }

    public class RotateDataProvider
    {
        public static IEnumerable RotateTestCases
        {
            get
            {
                yield return new TestCaseData(new int[] { 1, 2, 3, 4, 5, 6, 7 }, 3, new int[] { 5, 6, 7, 1, 2, 3, 4});
                yield return new TestCaseData(new int[] { 6, 7, 2, 44, 6, 5 }, 2, new int[] { 6, 5, 6, 7, 2, 44});
                yield return new TestCaseData(new int[] { 88, 55, 89, 90, 1, 45, 30, 12, 90, 6, 44, 43, 99, 5, 6 }, 8, new int[] { 12, 90, 6, 44, 43, 99, 5, 6, 88, 55, 89, 90, 1, 45, 30 });
            }
        }

        public static IEnumerable ReverseTestCases
        {
            get
            {
                yield return new TestCaseData(new int[] { 1, 2, 3, 4, 5, 6 }).Returns(new int[] { 6, 5, 4, 3, 2, 1 });
            }
        }
    }
}
