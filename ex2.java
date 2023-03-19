import java.util.Scanner;

public class ex2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite um número inteiro: ");
        int num = sc.nextInt();
        sc.close();

        // Inicialização das variáveis
        int fib_ant = 0;
        int fib_atual = 1;
        boolean pertence_fibonacci = false;

        // Verifica se o número pertence à sequência de Fibonacci
        while (fib_atual <= num) {
            if (fib_atual == num) {
                pertence_fibonacci = true;
                break;
            }
            int fib_prox = fib_ant + fib_atual;
            fib_ant = fib_atual;
            fib_atual = fib_prox;
        }

        // Imprime a mensagem indicando se o número pertence ou não à sequência de Fibonacci
        if (pertence_fibonacci) {
            System.out.println(num + " pertence à sequência de Fibonacci!");
        } else {
            System.out.println(num + " não pertence à sequência de Fibonacci!");
        }
    }
}