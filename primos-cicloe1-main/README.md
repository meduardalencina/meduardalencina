## Primos e gêmeos

### Números primos

Você sabe o que é um número primo? Um número primo é um número que existem apenas dois divisores que resultam em uma
divisão inteira: ele mesmo, e 1. Por exemplo, 2 é um número primo, pois apenas 2 e 1 são divisores de 2; 3 também é um
número primo, porque apenas 3 e 1 podem dividi-lo e resultar em um número inteiro.

Você pode usar o WolframAlpha para consultar os números primos em um intervalo de valores:
[link](https://www.wolframalpha.com/input/?i=prime+numbers+between+1+and+100)

Números primos são muito úteis, sendo utilizados em diversas aplicações computacionais, como criptografia, blockchains,
dentre outras. Não existe um método computacional eficiente para verificar se um número é primo ou não; geralmente é
necessário verificar, de `2` até `N/2` (sendo `N` o número em questão), se algum número divide inteiramente o número `N`.

Considere por exemplo o número 11. 11 é primo (só pode ser dividido por 1 e 11). Mas para verificar isso, você precisaria
escrever um algoritmo que

1. Percorre todos os números entre `2` e `N/2` (nesse caso `5`);
2. Checa se algum desses números gerou uma divisão inteira;
3. Se sim, `N` não é primo; se chegar ao fim do laço e nenhum número conseguir dividir, então `N` é primo.

### Números primos gêmeos

Da mesma maneira, outro mistério da matemática são os
[números primos gêmeos](https://pt.wikipedia.org/wiki/N%C3%BAmeros_primos_g%C3%A9meos). São números primos que estão
divididos por, no máximo, um valor entre eles. Por exemplo: 3 e 5 são números primos gêmeos, pois existe apenas o número
4 entre eles; 11 e 13 também são, pois só o 14 fica entre eles; e assim por diante. Você pode consultar todos os números
primos gêmeos entre um intervalo de valores usando o WolframAlpha:
[link](https://www.wolframalpha.com/input/?i=twin+prime+numbers+between+1+and+100)

## Descrição do trabalho

Seu objetivo é escrever duas funções:

* A primeira, de nome `is_prime`, deve receber um número como parâmetro, e dizer se aquele número é primo ou não.
  * Se o número for primo, a função deve retornar `true`
  * Se o número não for primo, a função deve retornar `false`  
* A segunda, de nome `twins_between_values`, deve receber dois números como parâmetro, e dizer quantos números primos
  gêmeos existem neste intervalo de valores.

Existem dois arquivos de código-fonte, [primes.c](src/primes.c) e [twins.c](src/twins.c). Desenvolva o código da primeira
função no arquivo `primes.c`, e o código da segunda função no arquivo `twins.c`. Não se esqueça de copiar o código da
primeira função para o segundo arquivo!

A assinatura das funções (ou seja, o tipo de retorno, tipo dos parâmetros, e número de parâmetros) já está correta, 
restando a você apenas desenvolver o código. Substitua as instruções de `return` pelo seu código.

Existem testadores para cada um dos arquivos de código-fonte. Deixe as funções main quietas! Rode elas para ver se
está desenvolvendo o código corretamente.

## Como entregar este trabalho

Você não precisa me entregar nada. Eu já tenho acesso ao seu repositório /mwahaha

**CONTUDO**, não esqueça de enviar as suas modificações para o repositório remoto do Github:

```
git add .
git commit -m "implementei a primeira função"
git push origin main
```

**VERIFIQUE** o seu repositório remoto para ter certeza que as modificações estão lá!

## Nota

Para este trabalho, a nota é muito simples. São duas funções, e cada uma vale metade da nota.
