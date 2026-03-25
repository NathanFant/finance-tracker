FINANCE TRACKER
===============

Purpose
-------
This repository is a TypeScript-first, full‑stack project using Bun.
Both frontend and backend are written in TypeScript, with shared types
to avoid duplication and drift.

This repo is intentionally framework-agnostic so future changes
(Node vs Bun, Vite vs Next, etc.) do NOT require a rewrite.


Repository Structure
--------------------

finance-tracker/
│
├─ apps/
│  ├─ web/            Frontend (React + Vite + TypeScript)
│  └─ api/            Backend (TypeScript, framework TBD)
│
├─ packages/
│  └─ shared/         Shared types, schemas, and utilities
│
├─ tsconfig.base.json Shared TypeScript config (frontend + backend)
├─ package.json       Root scripts and tooling
└─ bun.lockb          Bun dependency lockfile


Directory Guide
---------------

apps/web
  - React frontend
  - Built with Vite + TypeScript
  - Runs independently from backend
  - Safe to migrate to Next.js later

apps/api
  - Backend entry point
  - Currently plain TypeScript (no framework lock-in)
  - Can become:
      - Node (Express/Fastify)
      - Bun (Hono)
      - Next API routes

packages/shared
  - Code shared between frontend and backend
  - Types, interfaces, schemas, domain logic
  - Imported via path alias: @shared/*

tsconfig.base.json
  - Single source of truth for TypeScript configuration
  - Extended by frontend and backend tsconfigs
  - Enables shared paths and strict typing everywhere


Path Aliases
------------

The following alias is available across the project:

  @shared/*  -> packages/shared/src/*

This allows frontend and backend to import the same types safely.