# Algorithm Benchmark

Benchmark de algoritmos de ordenação e busca desenvolvido em C++ para comparar, na prática, o desempenho de diferentes algoritmos e relacioná-lo às suas respectivas complexidades computacionais.

## Objetivo

O projeto foi desenvolvido para estudar e demonstrar:

* Implementação de algoritmos clássicos em C++;
* Análise de complexidade de tempo;
* Diferença prática entre algoritmos O(n²), O(n log n), O(n) e O(log n);
* Medição de desempenho utilizando `std::chrono`;
* Geração de datasets para experimentos;
* Desenvolvimento de testes automatizados;
* Comparação entre diferentes estratégias algorítmicas.

O foco não é apenas implementar os algoritmos, mas observar como suas características teóricas aparecem nos resultados experimentais.

## Algoritmos implementados

### Ordenação

| Algoritmo      | Complexidade média | Complexidade de pior caso |
| -------------- | -----------------: | ------------------------: |
| Bubble Sort    |              O(n²) |                     O(n²) |
| Insertion Sort |              O(n²) |                     O(n²) |
| Merge Sort     |         O(n log n) |                O(n log n) |
| Quick Sort     |         O(n log n) |                     O(n²) |

### Busca

| Algoritmo     | Complexidade |
| ------------- | -----------: |
| Linear Search |         O(n) |
| Binary Search |     O(log n) |

A Binary Search exige que o vetor esteja previamente ordenado.

## Benchmark de ordenação

Foram utilizados datasets aleatórios com:

* 1.000 elementos;
* 5.000 elementos;
* 10.000 elementos.

Os tempos foram medidos diretamente pelo programa utilizando `std::chrono`.

### Resultados

| Dataset | Bubble Sort | Insertion Sort | Merge Sort | Quick Sort |
| ------: | ----------: | -------------: | ---------: | ---------: |
|   1.000 |    0,626 ms |       0,108 ms |   0,243 ms |   0,054 ms |
|   5.000 |   15,353 ms |       2,692 ms |   1,396 ms |   0,290 ms |
|  10.000 |   89,967 ms |      10,315 ms |   2,697 ms |   0,642 ms |

Os resultados mostram claramente a diferença entre algoritmos quadráticos e algoritmos baseados em divisão e conquista.

O Bubble Sort apresentou crescimento muito mais acentuado conforme o tamanho do dataset aumentou, enquanto Merge Sort e Quick Sort mantiveram tempos significativamente menores.

## Benchmark de busca

Para a comparação entre métodos de busca, foi utilizado um vetor ordenado com 100.000 elementos.

Resultado obtido:

| Algoritmo     |     Tempo |
| ------------- | --------: |
| Linear Search | 56.600 ns |
| Binary Search |    100 ns |

Neste experimento, o elemento procurado estava no final do vetor, criando uma situação desfavorável para a Linear Search.

A Binary Search conseguiu reduzir drasticamente o número de elementos analisados a cada etapa, demonstrando na prática a vantagem da complexidade O(log n).

## Como funciona

### Geração dos dados

Os datasets são gerados utilizando:

```cpp
std::mt19937
```

com uma seed fixa para tornar os experimentos reproduzíveis.

### Medição

O tempo de execução é medido utilizando:

```cpp
std::chrono
```

O benchmark copia o dataset original antes de cada ordenação para garantir que todos os algoritmos recebam os mesmos dados.

### Comparação

Cada algoritmo é executado sobre datasets de diferentes tamanhos e seus tempos são apresentados no terminal.

Isso permite observar experimentalmente como o crescimento da entrada afeta cada algoritmo.

## Testes

O projeto possui testes para verificar:

* Bubble Sort;
* Insertion Sort;
* Merge Sort;
* Quick Sort;
* Linear Search;
* Binary Search;
* Busca de elementos existentes;
* Busca de elementos inexistentes;
* Ordenação correta dos vetores.

Para executar os testes:

```powershell
g++ -std=c++17 -O2 algorithm-benchmark\tests\test_algorithms.cpp algorithm-benchmark\src\algorithms.cpp -o algorithm-benchmark\tests.exe
```

Depois:

```powershell
.\algorithm-benchmark\tests.exe
```

Resultado esperado:

```text
All algorithm tests passed!
```

## Como executar o benchmark

Compile o programa:

```powershell
g++ -std=c++17 -O2 algorithm-benchmark\src\main.cpp algorithm-benchmark\src\algorithms.cpp -o algorithm-benchmark\benchmark.exe
```

Execute:

```powershell
.\algorithm-benchmark\benchmark.exe
```

## Estrutura

```text
algorithm-benchmark/
│
├── src/
│   ├── algorithms.cpp
│   ├── algorithms.hpp
│   ├── benchmark.hpp
│   └── main.cpp
│
├── tests/
│   └── test_algorithms.cpp
│
└── README.md
```

## Tecnologias

* C++17
* GNU g++
* C++ Standard Library
* `std::vector`
* `std::algorithm`
* `std::chrono`
* `std::random`
* `assert`

## Conceitos demonstrados

Este projeto aborda conceitos importantes de Ciência da Computação e desenvolvimento de software:

* Estruturas de dados;
* Algoritmos de ordenação;
* Algoritmos de busca;
* Recursão;
* Divisão e conquista;
* Ponteiros para funções;
* Complexidade assintótica;
* Benchmarking;
* Testes automatizados;
* Análise experimental de desempenho.

## Limitações

Os tempos apresentados dependem do hardware, sistema operacional, compilador e condições de execução.

Por isso, os valores absolutos não devem ser interpretados como uma medida universal de desempenho. O principal objetivo do benchmark é observar as tendências de crescimento e comparar os algoritmos sob as mesmas condições.

Além disso, o Quick Sort utilizado possui uma estratégia simples de escolha de pivô e pode apresentar comportamento O(n²) em determinadas distribuições de entrada.

## Possíveis melhorias

Algumas extensões futuras incluem:

* Testar datasets ainda maiores;
* Comparar diferentes estratégias de escolha de pivô;
* Adicionar Heap Sort;
* Adicionar busca interpolada;
* Executar múltiplas repetições e calcular média e desvio padrão;
* Exportar resultados para CSV;
* Criar gráficos de desempenho;
* Automatizar os benchmarks;
* Comparar diferentes níveis de otimização do compilador.

## Conclusão

O projeto demonstra como a análise de complexidade pode ser observada experimentalmente através de benchmarks reais.

Os resultados mostram que algoritmos com melhor complexidade assintótica tendem a escalar muito melhor conforme o tamanho dos dados aumenta, destacando a importância da escolha de algoritmos em aplicações que trabalham com grandes volumes de informação.
