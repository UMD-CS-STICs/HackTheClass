all: assemble load run

assemble: hello.s
	yasm -felf32 hello.s

load: hello.o
	ld -m elf_i386 hello.o -o hello.x

run: hello.x
	./hello.x

disasmo: hello.o
	objdump -D -Mintel hello.o

disasmx: hello.x
	objdump -D -Mintel hello.x

clean:
	rm hello.o
	rm hello.x
