#!/usr/bin/env python3

from bcc import BPF
from pathlib import Path
from time import sleep

program = Path.cwd() / 'echo_uid.c'
with open(program, mode='r') as f:
    program_text = f.read()

b = BPF(text=program_text)
clone = b.get_syscall_fnname("clone")
b.attach_kprobe(event=clone, fn_name="capture_uids")

while True:
    sleep(2)
    for uid, count in b["user_ids"].items():
        print(f"UID {uid.value}: {count.value} count")

