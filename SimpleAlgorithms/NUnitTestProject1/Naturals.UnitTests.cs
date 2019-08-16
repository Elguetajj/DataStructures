using NUnit.Framework;
using System.Collections;
using SimpleAlgorithms;

namespace SImpleAlgorithmsTests
{
    [TestFixture]
    class NaturalsUnitTests
    {
        [Test, TestCaseSource(typeof(NaturalsDataProvider),"TestCases")]
        public int NaturalsTest(int n)
        {
            return Naturals.sumNaturals(n);
        }

        [Test, TestCaseSource(typeof(NaturalsDataProvider),"ExceptionTestCases")]
        public void NaturalsExceptionTest(int n)
        {
            var ex = Assert.Throws<System.ArgumentOutOfRangeException>(() => Naturals.sumNaturals(n));
            Assert.That(ex.Message, Is.EqualTo($@"Number must be a natural number
Parameter name: n"));
        }
    }

    public class NaturalsDataProvider
    {
        public static IEnumerable TestCases
        {
            get
            {
                yield return new TestCaseData(7).Returns(28);
                yield return new TestCaseData(10).Returns(55);
                yield return new TestCaseData(21).Returns(231);
                yield return new TestCaseData(100).Returns(5050);
            }
        }

        public static IEnumerable ExceptionTestCases
        {
            get
            {
                for (int i=-10; i < 0; i++)
                {
                    yield return new TestCaseData(i);
                }
            }
        }
    }
}
