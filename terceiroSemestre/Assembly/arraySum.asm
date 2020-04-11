.data 
vetor: .word 1, 3, 5, 7

saida: .asciiz "A soma do vetor �: "

.text
	la	$t0, vetor                      # Carrega os valores do vetor para o endere�o do registrador $t0
	li	$t2, 0                          # Inst�ncia de um registrador com valor zero
	li	$t3, 0                          # Inst�ncia de um registrador com valor zero

loop:					        # Soma todos os valores do vetor
	sltiu   $t7, $t2, 4			# Define o tamanho  do vetor
	beq     $t7, $0,  fim                   # Se $t7 for igual a $0, ele cai na fun��o fim
	lw      $t4, ($t0)			# Salva o conte�do do vetor em $t4
	addu    $t3, $t3, $t4                   # $t3 = $t3 + $t4
	addiu	$t0, $t0, 4                     # t0 += 4
	addiu   $t2, $t2, 1                     # t2 += 1
	j loop

fim:
	la	$a0, saida                      # Carrega para $a0 a string de sa�da 
	li	$v0, 4                        
	syscall                                 
	addu	$a0, $0, $t3			# Printa a soma do vetor
	li	$v0, 1
	syscall
	li	$v0, 10			        # Chama a sa�da do programa
	syscall
	
