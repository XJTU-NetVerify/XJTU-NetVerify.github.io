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

166 directories
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

```bash
rm -rf public; hugo server
```

runs on [localhost:1313](http://localhost:1313)

* use parameter `--disableFastRender` if needed
* cause it needs to convert and generate labels, you can restart the server if new class ([tailwind css](https://tailwindcss.com/docs)) or style makes no effect
