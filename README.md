# About

These are my initial experiments in [eBPF](https://ebpf.io/), inspired by [Liz Rice](http://www.lizrice.com/)'s [Beginner's Guide to eBPF](https://github.com/lizrice/ebpf-beginners), using [BPF Compiler Collection (BCC)](https://github.com/iovisor/bcc) on a [Debian](https://www.debian.org/) image running in [VirtualBox](https://www.virtualbox.org/) (to prevent any accidental kernel damage)

# Installation

- [Install VirtualBox](https://www.virtualbox.org/wiki/End-user_documentation)
- [Create a new Debian server image](https://www.google.com/search?hl=en&q=debian+on+virtualbox) (`debian-11.4.0-amd64-netinst.iso` worked just fine) and run it
- Within the running server image:
  - `apt-get install build-essential`
  - `apt-get install linux-headers-$(uname -r)`
  - [Install BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md#debian---binary): `apt-get install bpfcc-tools python3-bpfcc libbpfcc libbpfcc-dev`
  - clone this repo, and run the python scripts as a privileged user