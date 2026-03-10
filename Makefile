.PHONY: all

docs/themes/%.gif: docs/themes/%.tape
	vhs $<

tapes := $(wildcard docs/themes/*.tape)
targets := $(patsubst %.tape,%.gif,$(tapes))

all: $(targets)
