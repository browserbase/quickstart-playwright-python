<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="logo/light.svg"/>
        <img alt="Browserbase logo" src="logo/light.svg" width="300" />
    </picture>
</p>

<p align="center">
    <a href="https://docs.browserbase.com">Documentation</a>
    <span>&nbsp;·&nbsp;</span>
    <a href="https://www.browserbase.com/playground">Playground</a>
</p>
<br/>

## Playwright with Browserbase

## Introduction

Browserbase is the best developer platform to reliably run, manage, and monitor headless browsers.

Get browsers' complete control and leverage Browserbase's
[Infrastructure](https://docs.browserbase.com/under-the-hood), [Stealth Mode](https://docs.browserbase.com/features/stealth-mode), and
[Session Debugger](https://docs.browserbase.com/features/sessions) to power your automation, test suites,
and LLM data retrievals.

**Get started in under one minute** with Playwright.

## Setup

### 1. Install dependencies

```bash
uv sync
uv run playwright install chromium
```

### 2. Create `.env` file:

```bash
cp .env.example .env
```

### 3. Get your Browserbase API Key:

- [Create an account](https://www.browserbase.com/sign-up) or [log in to Browserbase](https://www.browserbase.com/sign-in)
- Copy your API Key [from your Settings page](https://www.browserbase.com/settings) into the `.env` file

### 4. Run the script:

```bash
uv run python main.py
```

## Further reading

- [Explore the Browserbase Python SDK](https://docs.browserbase.com/sdk/python)
- [Explore the Playwright Python API](https://playwright.dev/python/docs/api/class-page)
