.PHONY: all

%.gif: %.tape
	vhs $<

tapes := $(wildcard docs/cli/*.tape docs/themes/*.tape)
targets := $(patsubst %.tape,%.gif,$(tapes))

all: $(targets)
