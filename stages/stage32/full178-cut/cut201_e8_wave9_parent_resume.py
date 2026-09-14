#!/usr/bin/env python3
from __future__ import annotations

import cut201_e8_wave9_parent_resume_protocol_g8 as protocol

PROTOCOL_G8_BLOB = "a45c83dc0f02842fcf024faf269b65bd6e6f64f7"
EXACT_WORKER_BLOB = "a8be279ebc3bca4a383d4a81e4c04de7413b17b8"


class ExactWorkerCompat:
    """Expose exact worker metadata and its lower-level core through one read-only interface."""

    def __init__(self, worker):
        self._worker = worker
        self._engine = worker.core

    def __getattr__(self, name):
        if hasattr(self._worker, name):
            return getattr(self._worker, name)
        return getattr(self._engine, name)


_original_load_exact = protocol.load_exact


def load_exact_compat(exact_root):
    worker = _original_load_exact(exact_root)
    protocol.req(hasattr(worker, "core"), "exact CUT201 worker lost core engine export")
    protocol.req(hasattr(worker.core, "e8"), "exact CUT201 core lost e8 interface")
    return ExactWorkerCompat(worker)


protocol.load_exact = load_exact_compat


if __name__ == "__main__":
    protocol.main()
