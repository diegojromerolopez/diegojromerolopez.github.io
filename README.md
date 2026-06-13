# Diego J.'s Software Tar Pit

This repository contains the source code for [Diego J.'s blog](https://diegojromerolopez.github.io/), built using the [Hugo](https://gohugo.io/) static site generator.


---

## 🛠️ Prerequisites & Installation

To run and build this blog locally, you need to install **Hugo (Extended)**. The extended version is required because the blog's stylesheet setup uses Sass/SCSS compilation.

### macOS (via Homebrew)
If you have Homebrew installed on your mac, run:
```bash
brew install hugo
```
*(On macOS, Homebrew installs the extended version of Hugo by default. You can verify your installation by running `hugo version`—the output should contain `extended`.)*

---

## 🚀 Local Development

We provide a Python wrapper script at [bin/serve.py](file:///Users/diegoj/repos/diegojromerolopez.github.io/bin/serve.py) to make running and testing the blog easy.

### 1. Live Reload Development Server
To launch Hugo's native server in development mode (which enables draft posts and live-reload on save):
```bash
python3 bin/serve.py
```
Open your browser and navigate to:
👉 **[http://localhost:1313](http://localhost:1313)**

### 2. Static Production Server
To preview how the blog will look once compiled and minified (to test asset loading and absolute paths):
```bash
python3 bin/serve.py --static
```
This builds the site with minification to `./public` and spins up a local Python web server. Navigate to:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## ✍️ Creating a New Blog Post

This blog supports multi-language posting: English (`en`) and Spanish (`es`).

1. **Location**:
   - English posts: [content/en/post/](file:///Users/diegoj/repos/diegojromerolopez.github.io/content/en/post/)
   - Spanish posts: [content/es/post/](file:///Users/diegoj/repos/diegojromerolopez.github.io/content/es/post/)
2. **Naming Convention**: Use the format `YYYY-MM-DD-slug.md` (e.g. `2026-06-18-observability-with-isidorus.md`).
3. **Frontmatter**: Add a YAML block at the beginning of your markdown file:
   ```yaml
   ---
   title: "Your Post Title"
   date: "YYYY-MM-DDT00:00:00+02:00"
   draft: true
   tags: ["development", "hugo"]
   ---
   ```
   *(Keep `draft: true` while writing. Change to `draft: false` or remove the draft key when you are ready to publish.)*

---

## 🎨 Themes & Customization

The blog currently uses the [Anatole Theme](https://github.com/lxndrblz/anatole), which is tracked as a Git submodule under [themes/anatole/](file:///Users/diegoj/repos/diegojromerolopez.github.io/themes/anatole/).

### How to Change the Theme
To switch to a different Hugo theme:
1. Add the new theme repository as a submodule:
   ```bash
   git submodule add <theme-github-url> themes/<new-theme-name>
   ```
2. Update the theme field in [config.toml](file:///Users/diegoj/repos/diegojromerolopez.github.io/config.toml):
   ```toml
   theme = "new-theme-name"
   ```
3. Update any theme-specific variables inside the `[params]` section of [config.toml](file:///Users/diegoj/repos/diegojromerolopez.github.io/config.toml) to align with the new theme's requirements.
4. Verify that the site builds successfully and stylesheet compilation works by running:
   ```bash
   python3 bin/serve.py --static
   ```

---

## 🌐 Deployment (GitHub Actions)

Deployments are automated. Pushing any changes to the `master` branch triggers the GitHub Actions workflow in [.github/workflows/gh-pages.yml](file:///Users/diegoj/repos/diegojromerolopez.github.io/.github/workflows/gh-pages.yml). 

The pipeline:
1. Installs the extended version of Hugo (`0.163.1`).
2. Installs Dart Sass (needed for Anatole theme).
3. Builds and minifies the website.
4. Deploys the static files to the `gh-pages` branch.
