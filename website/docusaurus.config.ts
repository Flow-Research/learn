// docusaurus.config.ts
import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Flow Education Initiative',
  tagline: 'Powering the next generation of open-source contributors',
  favicon: 'img/favicon.ico',

  // GitHub Pages URL setup for the Flow-Research organization.
  // url: 'https://flow-research.github.io',
  // baseUrl: '/learn/',
  url: 'https://learn.flowresearch.tech',
  baseUrl: '/',
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
          sidebarItemsGenerator: async ({defaultSidebarItemsGenerator, ...args}) => {
            const items = await defaultSidebarItemsGenerator(args);
            type GeneratedSidebarItems = Awaited<ReturnType<typeof defaultSidebarItemsGenerator>>;
            const capitalize = (s: string) =>
              s.split(' ').map(w =>
                w.length > 0 && w !== w.toUpperCase()
                  ? w.charAt(0).toUpperCase() + w.slice(1)
                  : w
              ).join(' ');
            const processItems = (sidebarItems: GeneratedSidebarItems): GeneratedSidebarItems =>
              sidebarItems.map(item =>
                item.type === 'category'
                  ? {...item, label: capitalize(item.label), items: processItems(item.items)}
                  : item
              );
            return processItems(items);
          },
        },
        // Blog is drafted and preserved for future revival (see knowledge-base/articles/README.md).
        // Set to `false` to disable until ready. Uncomment the block below to re-enable.
        blog: false,
        // blog: {
        //   path: '../knowledge-base/articles',
        //   routeBasePath: 'blog',
        //   showReadingTime: true,
        //   editUrl: 'https://github.com/Flow-Research/learn/tree/main/',
        //   remarkPlugins: [remarkMath],
        //   rehypePlugins: [rehypeKatex],
        // },
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
        // Blog removed per 2026-05-20 meeting decision; preserved at knowledge-base/articles/
        {
href: 'https://github.com/Flow-Research',
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
            {label: 'GitHub', href: 'https://github.com/Flow-Research'},
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
