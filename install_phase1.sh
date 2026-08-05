#!/bin/bash

# Install core dependencies for frontend apps
pnpm --filter="@portfolio/web" add @tanstack/react-query zustand axios react-hook-form @hookform/resolvers zod next-themes lucide-react
pnpm --filter="@portfolio/admin" add @tanstack/react-query zustand axios react-hook-form @hookform/resolvers zod next-themes lucide-react

# Install schemas dependencies
pnpm --filter="@portfolio/schemas" add zod

# Install UI dependencies
pnpm --filter="@portfolio/ui" add lucide-react clsx tailwind-merge next-themes @radix-ui/react-slot
pnpm --filter="@portfolio/ui" add -D tailwindcss @types/node

# Install utils dependencies
pnpm --filter="@portfolio/utils" add axios @tanstack/react-query

