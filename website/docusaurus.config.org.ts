// docusaurus.config.ts
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Flow Education Initiative',
  tagline: 'Powering the next generation of African contributors',
  favicon: 'img/favicon.ico',

  url: 'https://flow-research.github.io',
  baseUrl: '/learn/',
  organizationName: 'Flow-Research',
  projectName: 'learn',
  trailingSlash: false,

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: '../curriculum', 
          routeBasePath: 'curriculum',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/creativebash/flow-learning/tree/main/',
        },
        blog: {
          path: '../knowledge-base/articles',
          routeBasePath: 'blog',
          showReadingTime: true,
          editUrl: 'https://github.com/creativebash/flow-learning/tree/main/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Flow Education',
      logo: {
        alt: 'Flow Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Curriculum',
        },
        {to: '/blog', label: 'Articles', position: 'left'},
        {
          href: 'https://github.com/creativebash/flow-learning',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learning',
          items: [
            {label: 'Curriculum', to: '/curriculum'},
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'Articles', to: '/blog'},
            {label: 'GitHub', href: 'https://github.com/creativebash/flow-learning'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Flow Education Initiative.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;