#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_THREADS   10

void *print_hello_word(void *tid){
    printf("Hello World. Greetings from thread %d\n\r", tid);
    pthread_exit(NULL);
}

int main (int argc, char *argv[]){
    pthread_t myThreads[NUMBER_OF_THREADS];
    int status, i;

    for (i=0; i < NUMBER_OF_THREADS; i++){
        printf("Programa principal, criando a thread %d\n\r",i);
        status = pthread_create(&myThreads[i], NULL, print_hello_word, (void *)i);

        if (status != 0 ){
            printf("Ops, erro ao criar a thread - error #%d\n\r", status);
            exit(-1);
        }
    }
    return 0;
}
