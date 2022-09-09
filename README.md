# About

These are my initial experiments in [eBPF](https://ebpf.io/), inspired by [Liz Rice](http://www.lizrice.com/)'s [Beginner's Guide to eBPF](https://github.com/lizrice/ebpf-beginners), using [BPF Compiler Collection (BCC)](https://github.com/iovisor/bcc) on a [Debian](https://www.debian.org/) image running in [VirtualBox](https://www.virtualbox.org/) (to prevent any accidental kernel damage, even though the [eBPF verifier](https://docs.kernel.org/bpf/verifier.html) is supposed to protect against it)

# Installation

- [Install VirtualBox](https://www.virtualbox.org/wiki/End-user_documentation)
- [Create a new Debian server image](https://www.google.com/search?hl=en&q=debian+on+virtualbox) (`debian-11.4.0-amd64-netinst.iso` worked just fine) and run it
- Within the running server image:
  - `apt-get install build-essential`
  - `apt-get install linux-headers-$(uname -r) linux-image-$(uname -r)`
  - [Install BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md#debian---binary) for use with the code in [bcc](bcc):
    - `apt-get install bpfcc-tools python3-bpfcc libbpfcc libbpfcc-dev`
  - Install source for [libbpf](libbpf) (hat tip to [Raymond P. Burkholder](https://github.com/rburkholder) for [these instructions](https://blog.raymond.burkholder.net/index.php?/archives/1000-eBPF-Basics.html)): 
    - `apt-get install linux-source bc kmod cpio flex libncurses5-dev libelf-dev libssl-dev dwarves rsync`
    - `apt-get install clang llvm`
    - `apt-get install libbpf-dev bpfcc-tools bpftrace`
    - `apt-get install elfutils libelf-dev libelf1`
    - `ln -s /usr/src/linux-source-{version} /usr/src/linux`
    - `cd /usr/src/linux`
    - `make oldconfig && make prepare && make all`
