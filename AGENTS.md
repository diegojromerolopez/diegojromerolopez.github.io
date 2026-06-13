# Agent Instructions & Guidelines

This document provides technical instructions, structural maps, and quality guardrails for Gemini and other AI coding assistants working on the **diegojromerolopez.github.io** repository ([Diego J.'s blog](https://diegojromerolopez.github.io/)).

---

## Tech Stack & Dependencies

- **Hugo (Extended)**: The blog is generated using the extended version of Hugo. 
  - The target version in production is `0.163.1`.
  - Extended version is required because the templates use Sass/SCSS compilation.
- **Dart Sass**: The build pipeline compiles stylesheets via Dart Sass. A native Dart Sass binary is installed during CI/CD to facilitate building.
- **Theme**: Currently using the [Anatole Theme](https://github.com/lxndrblz/anatole), integrated as a Git submodule.

---

## Directory Layout

- [config.toml](file:///Users/diegoj/repos/diegojromerolopez.github.io/config.toml) - Main Hugo configuration file. Defines languages (`en`/`es`), menus, permalinks, and params (e.g. social links, dark mode).
- [content/en/post/](file:///Users/diegoj/repos/diegojromerolopez.github.io/content/en/post/) - English blog posts.
- [content/es/post/](file:///Users/diegoj/repos/diegojromerolopez.github.io/content/es/post/) - Spanish blog posts.
- [themes/anatole/](file:///Users/diegoj/repos/diegojromerolopez.github.io/themes/anatole/) - Theme files (managed as a git submodule).
- [bin/serve.py](file:///Users/diegoj/repos/diegojromerolopez.github.io/bin/serve.py) - Python server wrapper used for local development and testing.
- [.github/workflows/gh-pages.yml](file:///Users/diegoj/repos/diegojromerolopez.github.io/.github/workflows/gh-pages.yml) - GitHub Actions deployment workflow. Builds using `hugo --minify` and deploys to `gh-pages` branch.

---

## How to Run the Blog Locally

To test pages and templates, use the Python wrapper script [bin/serve.py](file:///Users/diegoj/repos/diegojromerolopez.github.io/bin/serve.py):

### 1. Hugo Development Server (With Drafts and Live Reload)
To run Hugo's native server in development mode, run:
```bash
python3 bin/serve.py
```
This runs `hugo server -D` under the hood. The site will be available with live reload at:
`http://localhost:1313`

### 2. Static Production Server
To build the site static files and preview them exactly as they are deployed:
```bash
python3 bin/serve.py --static
```
This compiles the site with minification (`hugo --minify`) into `public/`, and then serves `public/` using Python's native HTTP server. The static site will be available at:
`http://localhost:8000`

---

## Content Guidelines

### Creating a New Post
Posts must follow the naming convention: `YYYY-MM-DD-slug.md`.
1. Place English posts under: [content/en/post/](file:///Users/diegoj/repos/diegojromerolopez.github.io/content/en/post/)
2. Place Spanish posts under: [content/es/post/](file:///Users/diegoj/repos/diegojromerolopez.github.io/content/es/post/)

#### Example Frontmatter
Posts must begin with YAML frontmatter containing:
```yaml
---
title: "Your Post Title"
date: "YYYY-MM-DDT00:00:00+02:00"
draft: true
tags: ["tag1", "tag2"]
---
```
*Note: The date is also extracted from the filename pattern due to the configuration rule in [config.toml](file:///Users/diegoj/repos/diegojromerolopez.github.io/config.toml#L53) (`date = [':filename', ':default']`), but explicitly writing it in the frontmatter is recommended for consistency.*

---

## Guidelines for Changing the Theme

To replace or upgrade the theme of the blog:
1. **Register the New Theme as a Submodule**:
   Ensure you add the theme as a Git submodule instead of a plain directory copy:
   ```bash
   git submodule add <theme-github-url> themes/<new-theme-name>
   ```
2. **Modify Configuration**:
   Update the `theme` field in [config.toml](file:///Users/diegoj/repos/diegojromerolopez.github.io/config.toml):
   ```toml
   theme = "new-theme-name"
   ```
   Be sure to translate or move theme-specific parameters (e.g. social menu structure, stylesheets, layouts) from the old theme settings to the new theme's supported format.
3. **Verify Sass Pipeline**:
   Since the CI/CD pipeline requires Dart Sass compilation, confirm the new theme builds without SCSS/Sass compilation errors by running `python3 bin/serve.py --static` locally.

---

## Mandatory Quality Guardrails for AI Editors

1. **Verify Builds Before Committing**: Always run `python3 bin/serve.py --static` to check for compilation errors, incorrect Go HTML template layouts, or broken asset paths.
2. **Preserve Existing Content**: Never overwrite or delete existing markdown files or resources in the `content/` folder without explicit instruction from the user.
3. **Keep Code References Clickable**: All markdown documentation files must contain absolute `file://` scheme links to referenced source code and configuration files when mentioned.
4. **Follow Language Isolation**: Ensure English posts remain under `content/en/post/` and Spanish posts under `content/es/post/`. Do not mix language locations.
