import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const AreaList = [
  {
    label: 'Foundations',
    title: 'Engineering fluency',
    detail:
      'Reading, documentation, version control, collaboration, and the mindset needed to work in public.',
    meta: '9 lessons',
  },
  {
    label: 'Blockchain',
    title: 'Decentralized infrastructure',
    detail:
      'Consensus, smart contracts, security, scalability, and protocol economics from beginner to advanced.',
    meta: '18 lessons',
  },
  {
    label: 'AI/ML',
    title: 'Production-minded machine learning',
    detail:
      'Math, pipelines, lifecycle, notebooks, libraries, MLOps, architectures, and applied research practice.',
    meta: '18 lessons',
  },
  {
    label: 'Protocol Engineering',
    title: 'Systems that coordinate',
    detail:
      'State machines, specifications, resilience, governance, performance, and enterprise-grade adoption.',
    meta: '18 lessons',
  },
];

const ProductList = [
  {
    label: 'Jarvis',
    detail: 'Agent runtime that spawns, configures, and secures Personal Operators.',
    icon: 'J',
  },
  {
    label: 'Garden',
    detail: 'Human-agent workspace with connected tools, workflows, and approvals.',
    icon: 'G',
  },
  {
    label: 'WorkStream',
    detail: 'Task pipeline that distributes work, verifies output, and handles rewards.',
    icon: 'W',
  },
  {
    label: 'Harnessy',
    detail: 'Reliability layer for testing, evaluating, and improving agent behavior.',
    icon: 'H',
  },
];

const PracticeList = [
  'Read technical material like a builder, not a passive student.',
  'Move from concept notes into reproducible labs and visible artifacts.',
  'Explain tradeoffs clearly across AI, blockchain, and distributed systems.',
  'Build toward open-source contribution instead of isolated coursework.',
  'Earn points and reputation through verified public contributions.',
];

function HeroSection() {
  return (
    <header className={styles.heroBanner}>
      <div className="container">
        <div className={styles.heroContent}>
          <div className={styles.heroEyebrow}>Flow Research</div>
          <Heading as="h1" className={styles.heroTitle}>
            Learn. <span className={styles.heroTitleAccent}>Build.</span> Contribute.
          </Heading>
          <p className={styles.heroSubtitle}>
            Flow Research builds Personal Operators — capable agents for people and
            enterprises. This curriculum teaches the skills to contribute to building
            them across AI/ML, blockchain, and protocol infrastructure.
          </p>
          <div className={styles.heroActions}>
            <Link className={styles.mainCta} to="/curriculum/curriculum-intro">
              Start learning
            </Link>
            <Link className={styles.secondaryCta} to="https://github.com/Flow-Research">
              Explore Flow
            </Link>
          </div>
          <dl className={styles.heroStats} aria-label="Key features">
            <div>
              <dt>Open source</dt>
            </div>
            <div>
              <dt>Free</dt>
            </div>
            <div>
              <dt>Self-paced</dt>
            </div>
          </dl>
        </div>
      </div>
    </header>
  );
}

function ProductsSection() {
  return (
    <section className={styles.sectionAlt}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <div className={styles.sectionKicker}>Products</div>
          <Heading as="h2">A system, not a collection</Heading>
          <p>
            Flow's products form one system: Jarvis gives the agent life, Garden gives
            it a workspace, WorkStream gives it valuable work, and Harnessy makes it
            reliable. Contributors help build every layer.
          </p>
        </div>
        <div className={styles.productGrid}>
          {ProductList.map((product) => (
            <article className={styles.productCard} key={product.label}>
              <div className={styles.productIcon}>{product.icon}</div>
              <p className={styles.productLabel}>{product.label}</p>
              <p>{product.detail}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function AreasSection() {
  return (
    <section className={styles.section}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <div className={styles.sectionKicker}>Curriculum</div>
          <Heading as="h2">A clear path from fundamentals to contribution</Heading>
          <p>
            The curriculum is organized around the capabilities you need to
            contribute to building Flow's products — from foundations through
            production-ready systems.
          </p>
        </div>
        <div className={styles.areaGrid}>
          {AreaList.map((area) => (
            <article className={styles.areaCard} key={area.label}>
              <div className={styles.areaMeta}>{area.meta}</div>
              <p className={styles.areaLabel}>{area.label}</p>
              <h3>{area.title}</h3>
              <p>{area.detail}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function PracticeSection() {
  return (
    <section className={styles.sectionAlt}>
      <div className="container">
        <div className={styles.practiceLayout}>
          <div>
            <div className={styles.sectionKicker}>Learning model</div>
            <Heading as="h2">Built for builders who learn by making things real</Heading>
            <p className={styles.practiceIntro}>
              Flow is not a content library for passive reading. Each area is
              designed to help learners turn concepts into notes, code,
              diagrams, experiments, and public contributions.
            </p>
            <Link className={styles.textLink} to="/curriculum/curriculum-intro">
              Browse the full curriculum
            </Link>
          </div>
          <ul className={styles.practiceList}>
            {PracticeList.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

function CtaSection() {
  return (
    <section className={styles.ctaSection}>
      <div className="container">
        <div className={styles.ctaBand}>
          <div>
            <div className={styles.sectionKicker}>Launch-ready learning</div>
            <Heading as="h2">Start with the curriculum, then contribute in public.</Heading>
          </div>
          <Link className={styles.bandCta} to="/curriculum/curriculum-intro">
            Enter curriculum
          </Link>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="Learn. Build. Contribute."
      description="Flow Research builds Personal Operators — capable agents for people and enterprises. This curriculum teaches the skills to contribute to building them.">
      <HeroSection />
      <main>
        <ProductsSection />
        <AreasSection />
        <PracticeSection />
        <CtaSection />
      </main>
    </Layout>
  );
}
