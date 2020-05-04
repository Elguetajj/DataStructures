# Sorting & Searching 

## Sorting
Para nuestra discusión tendremos en cuenta solo selection sort (ss), bubble sort (bs) y heap sort (hs). Esta tabla nos enseña la complejidad de tiempo y memoria de cada uno de estos algoritmos. 

![Sorting Complexity](./images/sorting.png "Sorting Complexity")


Los algoritmos se probaron con 3 tipos de inputs diferentes. 


### Random Input
![Random Input Sorting](./images/random_sorting.png "Results of sorting with random input")

### Few Unique Sorting

![Few Unique Input Sorting](./images/few_unique_sorting.png "Results of sorting with few unique input")





### Reversed Sorting

![Reversed Input Sorting](./images/reversed_sorting.png "Results of sorting with reversed input")




Los resultados de estos benchmarking son consistentes con la tabla para todos los inputs probados. En todos los casos Heap Sort es el mas rapido, seguido de Selection Sort y en ultimo lugar Bubble sort.


## Searching
Para nuestra discusión tendremos en cuenta los algoritmos de linear search, jump search y binary search. Esta tabla nos enseña la complejidad de tiempo. 

![Searching](./images/searching.png "Searching Complexity")


Para probar los algoritmos se utiliso una lista ya ordenada. Los resultados de el benchmark no fueron completamente consistentes al repetir el benchmark varias veces. 

![Searching](./images/search.png "Searching Complexity")


Como podemos ver Linear search tiene semi-consistentemente los peores tiempos. Sin embargo, Binary Search y Jump Search se pelean por el pimer y segundo lugar.   