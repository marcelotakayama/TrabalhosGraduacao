.data
	entrada: .asciiz "Digite um número: \n"
	saida: .asciiz "O fatorial é "

.text
	li $v0, 4
	la $a0, entrada
	syscall
	li $v0, 5
	syscall
	move $a0, $v0
	jal fatorial                            
	move $t0, $v0     
	li $v0, 4
	la $a0, saida
	syscall
	li $v0, 1        
	move $a0, $t0       
	syscall                                     
	li $v0, 10       
	syscall

fatorial:
	addi $t1, $t1, -8
	sw $s0, 4($t1)
	sw $ra, 0($t1)
	bne $a0, 0, else
	addi $v0, $zero, 1                      
	j fact_return

else:
	move $s0, $a0
	addi $a0, $a0, -1                        
	jal fatorial
	multu $s0, $v0                            
	mflo $v0

fact_return:
	lw $s0, 4($t1)
	lw $ra, 0($t1)
	addi $t1, $t1, 8
	jr $ra
