// docusaurus.config.ts
import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
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

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themes: ['@docusaurus/theme-mermaid'],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.45/dist/katex.min.css',
      type: 'text/css',
    },
  ],

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
          editUrl: 'https://github.com/Flow-Research/learn/tree/main/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
          path: '../knowledge-base/articles',
          routeBasePath: 'blog',
          showReadingTime: true,
          editUrl: 'https://github.com/Flow-Research/learn/tree/main/',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/flow_education_social_card.jpg',
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
          href: 'https://github.com/Flow-Research/learn',
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
            {label: 'Curriculum', to: '/curriculum/curriculum-intro'},
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'Articles', to: '/blog'},
            {label: 'GitHub', href: 'https://github.com/Flow-Research/learn'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Flow Education Initiative.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'python', 'powershell', 'yaml'],
    },
    mermaid: {
      theme: {light: 'neutral', dark: 'dark'},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
