CLANG = clang

EXECABLE = hello-bpf-monitor

BPFCODE = hello_kernel

BPFTOOLS = /usr/src/linux/samples/bpf
BPFLOADER = $(BPFTOOLS)/bpf_load.c

BPFTEST = /usr/src/linux/tools/testing/selftests/bpf/trace_helpers.c

CCINCLUDE += -I/usr/src/linux-headers-$(shell uname -r)-common/include     
CCINCLUDE += -I/usr/include/$(shell uname -m)-linux-gnu
CCINCLUDE += -I/usr/src/linux/tools/bpf/resolve_btfids/libbpf
CCINCLUDE += -I/usr/src/linux/tools/lib/bpf
CCINCLUDE += -I/usr/src/linux/tools/testing/selftests/bpf

LOADINCLUDE += -I/usr/src/linux/samples/bpf
LOADINCLUDE += -I/usr/src/linux/tools/lib
LOADINCLUDE += -I/usr/src/linux/tools/perf
LOADINCLUDE += -I/usr/src/linux/tools/include
LOADINCLUDE += -I/usr/src/linux/tools/testing/selftests/bpf

LIBRARY_PATH = -L/usr/local/lib64
BPFSO = -lbpf

# Setting -DHAVE_ATTR_TEST=0 for the kernel containing below patch:
# 06f84d1989b7 perf tools: Make usage of test_attr__* optional for perf-sys.h
CFLAGS += $(shell grep -q "define HAVE_ATTR_TEST 1" /usr/src/linux/tools/perf/perf-sys.h \
                  && echo "-DHAVE_ATTR_TEST=0")

.PHONY: clean $(CLANG) bpfload build

clean:
	rm -f *.o *.so $(EXECABLE)

build: ${BPFCODE.c} ${BPFLOADER}
	$(CLANG) -O2 -target bpf -c $(BPFCODE:=.c) $(CCINCLUDE) -o ${BPFCODE:=.o}

bpfload: build
	clang $(CFLAGS) -o $(EXECABLE) -lelf $(LOADINCLUDE) $(LIBRARY_PATH) $(BPFSO) \
        $(BPFLOADER) $(BPFTEST) hello_loader.c

$(EXECABLE): bpfload

.DEFAULT_GOAL := $(EXECABLE)
