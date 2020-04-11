.data
print1: .asciiz"\nO fatorial de "
print11: .asciiz"é"
print2: .asciiz"Digite um número: "
espaco: .asciiz" "

.text 
li $t1, 1
la $a0, print2
li $v0, 4

li $v0, 5
syscall
move $t0, $v0
move $t3, $t0

beq $t0, $zero, PRINT
CAL:
mul $t1, $t1, $t0
addi $t0, $t0, -1
bgtz $t0, CAL
PRINT:
la $a0, print1
li $v0, 4
syscall

la $a0, print11
li $v0, 4
syscall

la $a0, espaco
