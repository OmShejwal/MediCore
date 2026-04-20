# VaidyaAI Frontend

This folder contains the VaidyaAI web client built with Vite, React, TypeScript, and Tailwind CSS. It includes the main dashboard, AROMI coach, SahayakAI, ManasMitra, diagnosis pages, settings, and supporting UI components.

## What is included

- `src/pages` - top-level screens and workflows.
- `src/components` - shared UI and feature components.
- `src/services/api.ts` - Axios client that injects the bearer token and talks to the backend.
- `src/data` - local scheme data and other static content.
- `public` - static assets, redirects, and favicon files.

## Running Locally

1. Install dependencies.

```bash
npm install
```

2. Start the dev server.

```bash
npm run dev
```

3. Open `http://localhost:8080`.

## Backend Connection

- The Vite dev server proxies `/api` requests to `http://localhost:8002`.
- Authentication tokens are stored in `localStorage` under the `token` key.
- If the backend URL changes, update [vite.config.ts](vite.config.ts).

## Available Scripts

- `npm run dev` - start the local dev server.
- `npm run build` - build the production bundle.
- `npm run preview` - preview the production build locally.
- `npm run lint` - run ESLint.
- `npm test` - run Vitest.

## Frontend Environment

Create a local `.env` file if you need to override the backend URL.

```bash
VITE_API_URL=http://localhost:8002
```

If `VITE_API_URL` is not set, the app falls back to the built-in proxy path.

## Deployment Notes

- `Dockerfile.aws` and `nginx.aws.conf` support container-based AWS deployment.
- `vercel.json` and `netlify.toml` are included for static hosting setups.
- Make sure the production backend URL is reflected in your deployment env vars.

## Troubleshooting

- If chat pages show connection errors, confirm the backend is running on port `8002`.
- If protected pages redirect unexpectedly, clear `localStorage` and sign in again.
- If images or assets fail to load, verify the static files in `public` are present in the build.
