// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-talks",
          title: "Talks",
          description: "Highlighted academic talks and conference presentations.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/talks/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-outreach",
          title: "Outreach",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/outreach/";
          },
        },{id: "nav-articles",
          title: "Articles",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/articles/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-for-fun",
          title: "For Fun",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/forfun/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "I am the main author of unimpeded and a contributing author of anesthetic.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-people",
          title: "People",
          description: "The Handley Research Group",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "post-google-gemini-updates-flash-1-5-gemma-2-and-project-astra",
        
          title: 'Google Gemini updates: Flash 1.5, Gemma 2 and Project Astra <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "We’re sharing updates across our Gemini family of models and a glimpse of Project Astra, our vision for the future of AI assistants.",
        section: "Posts",
        handler: () => {
          
            window.open("https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/", "_blank");
          
        },
      },{id: "articles-bluesci-issue-64-the-loneliest-places-in-the-universe",
          title: 'BlueSci Issue 64 — The Loneliest Places in the Universe',
          description: "Contributing author to the 64th Issue of BlueSci, the University of Cambridge&#39;s longest-running science communication magazine",
          section: "Articles",handler: () => {
              window.location.href = "/articles/bluesci64/";
            },},{id: "articles-cambridge-university-astronomical-society-neptune-2026",
          title: 'Cambridge University Astronomical Society Neptune 2026',
          description: "Author of an article for Neptune, the annual magazine of the Cambridge University Astronomical Society",
          section: "Articles",handler: () => {
              window.location.href = "/articles/neptune2026/";
            },},{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "forfun-cuhkpgsa",
          title: 'CUHKPGSA',
          description: "Social Officer at the Cambridge University Hong Kong Postgraduate Scholars Association (2025-2026)",
          section: "Forfun",handler: () => {
              window.location.href = "/forfun/cuhkpgsa/";
            },},{id: "forfun-joy-luck-club",
          title: 'Joy Luck Club',
          description: "Committee Member at the Cambridge University Joy Luck Club (2025-2026)",
          section: "Forfun",handler: () => {
              window.location.href = "/forfun/joyluckclub/";
            },},{id: "news-new-paper-on-arxiv-the-bayesian-view-of-desi-dr2-evidence-and-tension-in-a-combined-analysis-with-cmb-and-supernovae-across-cosmological-models-a-bayesian-reanalysis-of-desi-dr2-data-showing-that-the-preference-for-extended-dark-energy-models-is-eliminated-when-using-planck-cmb-data-alone-arxiv-2603-05472",
          title: 'New paper on arXiv: The Bayesian view of DESI DR2: Evidence and tension...',
          description: "",
          section: "News",},{id: "news-invited-guest-speaker-two-week-fully-funded-academic-visit-to-the-university-of-tokyo",
          title: 'Invited Guest Speaker: two-week fully funded academic visit to the University of Tokyo....',
          description: "",
          section: "News",},{id: "news-accepted-for-two-contributed-talks-in-the-national-astronomical-meeting-nam-2026",
          title: 'Accepted for two contributed talks in the National Astronomical Meeting (NAM) 2026.',
          description: "",
          section: "News",},{id: "news-elected-a-fellow-of-the-royal-astronomical-society",
          title: 'Elected a Fellow of the Royal Astronomical Society.',
          description: "",
          section: "News",},{id: "outreach-stargazing",
          title: 'Stargazing',
          description: "Observations at the Institute of Astronomy",
          section: "Outreach",handler: () => {
              window.location.href = "/outreach/stargazing/";
            },},{id: "projects-anesthetic",
          title: 'anesthetic',
          description: "A Python package for processing nested sampling and MCMC chains",
          section: "Projects",handler: () => {
              window.location.href = "/projects/anesthetic/";
            },},{id: "projects-star-formation-in-galactic-outflows",
          title: 'Star Formation in Galactic Outflows',
          description: "Evidence for star formation inside galactic outflows from X-shooter observations",
          section: "Projects",handler: () => {
              window.location.href = "/projects/starformation/";
            },},{id: "projects-unimpeded",
          title: 'unimpeded',
          description: "A public nested sampling database for Bayesian cosmology",
          section: "Projects",handler: () => {
              window.location.href = "/projects/unimpeded/";
            },},{
        id: 'social-ads_library_id',
        title: 'Ads_library_id',
        section: 'Socials',
        handler: () => {
          window.open("", "_blank");
        },
      },{
        id: 'social-arxiv',
        title: 'arXiv',
        section: 'Socials',
        handler: () => {
          window.open("https://arxiv.org/a/ong_d_2.html", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%64%6C%6F%32%36@%63%61%6D.%61%63.%75%6B", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/DilyOng", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/dily-duan-yi-ong-3365b7152", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0009-0003-9958-8827", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=VQCtcUYAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
