import os,time
if os.environ.get("RECOVERY_READY") != "ready":
    raise RuntimeError("Missing required runtime variables for recovery-worker: RECOVERY_READY")
print("e2e-nas161-a61f recovery worker ready",flush=True)
time.sleep(86400)
