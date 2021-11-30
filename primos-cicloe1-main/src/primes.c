#include <stdbool.h>
#include <stdio.h>
#define N_PRIMES 10

bool is_prime(int number) {
	
	for (int i = 2; i <= number / 2; i++){	
    if (number % i == 0) {
    	return false;
    }
}
 	return true;
}

/**
 * Essa função main é o seu testador. Não modifique ela!
 */
int main() {
    int some_primes[N_PRIMES] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

    bool failure = false;
    for(int i = 0; i < N_PRIMES; i++) {
        if(!is_prime(some_primes[i])) {
            printf("Incorreto: %d\n", some_primes[i]);
            failure = true;
        } else {
            printf("  Correto: %d\n", some_primes[i]);
        }
    }

    return failure;
}
