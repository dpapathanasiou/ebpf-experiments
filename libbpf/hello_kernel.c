#include <linux/bpf.h>
//#include "libbpf/src/bpf_helpers.h"
#include "bpf_helpers.h"

SEC("tracepoint/syscalls/sys_enter_execve")
int bpf_prog(void *ctx) {
  char msg[] = "Hello, BPF World!";
  bpf_trace_printk(msg, sizeof(msg));
  return 0;
}

char _license[] SEC("license") = "GPL";
