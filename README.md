# Lab Homepage

## Structure

```bash
.
├── archetypes
├── content
│   ├── news
│   ├── papers
│   ├── people
│   └── zh
├── public
├── static
│   ├── intro
│   ├── joinus
│   ├── papers
│   └── people
└── themes
    └── blist
```

* `archetypes`: template
* `content`
    * `content/news`: news listed on index without href and image. only title, date, description will be shown
    * `content/papers`: publications. if the author in people -> use id, else if has own homepage -> use url, else -> omit
    * `content/people`: layout 'people' or 'mentor'
    * `content/zh`: Chinese version now only support index and about
* `public`: use `rm -rf public; hugo server` to re-render this project
* `static`: all static resources. make the `public` directory clear by setting the same dir name
* `theme`: submodule. access on [https://github.com/Augists/blist-hugo-theme](https://github.com/Augists/blist-hugo-theme)

## Build

### Clone

```bash
git clone git@github.com:XJTU-NetVerify/XJTU-NetVerify.github.io.git --recurse-submodules
```

Download with all [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) init and update

Check that theme project `themes/blist` has been prepared

### Run

```bash
rm -rf public; hugo server
```

runs on [localhost:1313](http://localhost:1313)

* use parameter `--disableFastRender` if needed
* cause it needs to convert and generate labels, you can restart the server if new class ([tailwind css](https://tailwindcss.com/docs)) or style makes no effect

## GitHub Actions

Now the project is powered by GitHub Actions. Check `.github/workflows/gh-pages.yml`

1. Setup Hugo with version 0.125.4 (same as development environment)
2. Setup Node.js and NPM with version 20
3. Download packages
4. `hugo` (`--minify`) for deployment 
    * **replace baseurl in `hugo.toml`**
    * deploy on branch `gh-pages` (for GitHub Pages)
