from random import sample,choices
import pytest
from sorting import selection_sort, bubble_sort, heapSort

random_sample = sample(range(1, 1000), 999)
few_unique_sample = choices(range(1,5),k=999)
sorted_few_unique = sorted(few_unique_sample)

sorted_list = list(range(1, 1000))

reversed_sample = list(reversed(sorted_list))


@pytest.mark.random
def test_ss_random(benchmark):
    result = benchmark(selection_sort, random_sample)
    assert result == sorted_list

@pytest.mark.random
def test_bs_random(benchmark):
    result = benchmark(bubble_sort, random_sample)
    assert result == sorted_list

@pytest.mark.random
def test_hs_random(benchmark):
    result = benchmark(heapSort, random_sample)
    assert result == sorted_list


@pytest.mark.few_unique
def test_ss_few_unique(benchmark):
    result = benchmark(selection_sort, few_unique_sample)
    assert result == sorted_few_unique

@pytest.mark.few_unique
def test_bs_few_unique(benchmark):
    result = benchmark(bubble_sort, few_unique_sample)
    assert result == sorted_few_unique

@pytest.mark.few_unique
def test_hs_few_unique(benchmark):
    result = benchmark(heapSort, few_unique_sample)
    assert result == sorted_few_unique



@pytest.mark.reversed
def test_ss_reversed(benchmark):
    result = benchmark(selection_sort, reversed_sample)
    assert result == sorted_list

@pytest.mark.reversed
def test_bs_reversed(benchmark):
    result = benchmark(bubble_sort, reversed_sample)
    assert result == sorted_list

@pytest.mark.reversed
def test_hs_reversed(benchmark):
    result = benchmark(heapSort, reversed_sample)
    assert result == sorted_list



