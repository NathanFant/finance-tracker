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


Bun Commands (Most Important Section)
------------------------------------

Check Bun installation and version:
  bun --version
  Confirms Bun is installed and accessible.

Initialize dependencies:
  bun install
  Installs dependencies listed in package.json.

Add a dependency:
  bun add <package>
  Installs a runtime dependency.

Add a dev dependency:
  bun add -D <package>
  Installs a development-only dependency.

Remove a dependency:
  bun remove <package>
  Removes a dependency from the project.

Run a file directly:
  bun run path/to/file.ts
  Runs a TypeScript file with no build step.

Upgrade Bun:
  bun upgrade
  Updates Bun to the latest version.


Project-Specific Commands
-------------------------

Run the frontend (React):
  bun run --cwd apps/web dev

Starts the Vite dev server for the React app.

Run the backend:
  bun run apps/api/src/index.ts

Runs the backend entry file directly.

Run both frontend and backend:
  bun dev

Uses the root package.json script to start both.


Navigation Tips (Terminal Sanity)
---------------------------------

Go to project root:
  cd /workspaces/finance-tracker

Go to frontend:
  cd apps/web

Go to backend:
  cd apps/api

Go back to last directory:
  cd -

Show current directory:
  pwd

Run commands without changing directories:
  bun run --cwd apps/web dev


Design Principles (Why This Is Set Up This Way)
-----------------------------------------------

- TypeScript everywhere (frontend + backend)
- Shared types to avoid duplication
- No early framework lock-in
- Easy migration to Next.js if needed
- Minimal tooling, maximum clarity
- Optimized for future maintainability


Future Notes
------------

Likely next steps for this project:
- Choose backend framework (Hono / Express / Next)
- Add API contracts (zod or tRPC)
- Connect frontend to backend
- Add persistence (DB)
- Add auth if needed

This README exists so future-you can context-switch
into this project quickly without re-learning decisions.


=============