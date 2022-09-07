BPF_HASH(user_ids);

int capture_uids(void *ctx) {
   u64 uid;
   u64 counter = 0;
   u64 *p;

   uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
   p = user_ids.lookup(&uid);
   if (p != 0) {
      counter = *p;
   }

   counter++;
   user_ids.update(&uid, &counter);

   return 0;
}