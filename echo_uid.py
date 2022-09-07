#!/usr/bin/env python3

from bcc import BPF
from time import sleep

with open("echo_uid.c") as f:
    program = f.read()

b = BPF(text=program)
clone = b.get_syscall_fnname("clone")
b.attach_kprobe(event=clone, fn_name="capture_uids")

while True:
    sleep(2)
    for k,v in b["user_ids"].items():
        print("ID {}:\t{}\n".format(k.value, v.value))

