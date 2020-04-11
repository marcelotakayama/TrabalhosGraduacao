.data
    vetor: .word 5, 2, 10
    ler1: .asciiz"\nO maior número é: "
    ler2: .asciiz"\nO menor número é: "
    ler3: .asciiz"\nO número do meio é:  "
    espaco: .asciiz"  "

.text
    la $t0,vetor
    li $t1, 0
    la $t8,vetor
    la $t2, vetor
    li $t3,3
    lw $t5,0($t0)                         #maior
    lw $t6,0($t0)                         #menor
    lw $t9,0($t0)                         #meio

loop:
     beq $t1,$t3,saida                    #Compara o tamanho do vetor com o tamanho do registrador
     lw $t4,0($t0)                        #Carrega o vetor para o registrador $t4

     move $a0, $t4                        #Move o vetor para $a0
     li $v0,1
     syscall

     la $a0,espaco                        #Printa o vetor de forma mais visual
     li $v0,4
     syscall

     lw $t7,0($t8)                        #Carrega o vetor para $t7
     lw $s2,0($t2)                        #Carrega o vetor para $s2
     
     addi $t1,$t1,1
     addi $t0,$t0,4
     addi $t8,$t8,4
     bgt $t4,$t5,guardaMaior             #Compara se $t4 é maior que $t5
     blt $t7,$t6,guardaMenor             #Compara se $t7 é menor que $t6
     else: blt $t9,$t5,guardaMeio        #Faz o else dos dois operadores acima
     j loop
guardaMaior:
     move $t5,$t4
     j loop
guardaMenor:
    move $t6,$t7
    j loop
guardaMeio:
    move $t9,$s2
    j loop
saida:
    la $a0,ler1                        #Chamada da função ler1 e guardaMaior
    li $v0,4
    syscall

    move $a0, $t5
    li $v0,1
    syscall

    la $a0,ler2                        #Chamada da função ler2 e guardaMenor
    li $v0,4
    syscall

    move $a0, $t6
    li $v0,1
    syscall
    
    la $a0,ler3                        #Chamada da função ler3 e guardaMeio
    li $v0,4
    syscall

    move $a0, $t9
    li $v0,1
    syscall