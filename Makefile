# These targets are not files
.PHONY: tests

tests:
	./bin/test

tools:
	git clone https://github.com/nfeliciano/rightnow
