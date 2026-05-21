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
  },
  {
    label: 'Garden',
    detail: 'Human-agent workspace with connected tools, workflows, and approvals.',
  },
  {
    label: 'WorkStream',
    detail: 'Task pipeline that distributes work, verifies output, and handles rewards.',
  },
  {
    label: 'Harnessy',
    detail: 'Reliability layer for testing, evaluating, and improving agent behavior.',
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
          <p className={styles.heroEyebrow}>Flow Research</p>
          <Heading as="h1" className={styles.heroTitle}>
            Build public good technology in the open.
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
            <Link className={styles.secondaryCta} to="/blog">
              Read articles
            </Link>
          </div>
          <dl className={styles.heroStats} aria-label="Curriculum summary">
            <div>
              <dt>64</dt>
              <dd>lessons</dd>
            </div>
            <div>
              <dt>5</dt>
              <dd>areas</dd>
            </div>
            <div>
              <dt>4</dt>
              <dd>products</dd>
            </div>
          </dl>
        </div>
      </div>
    </header>
  );
}

function ProductsSection() {
  return (
    <section className={styles.productsSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <p className={styles.sectionKicker}>Products</p>
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
    <section className={styles.areasSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <p className={styles.sectionKicker}>Curriculum</p>
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
    <section className={styles.practiceSection}>
      <div className="container">
        <div className={styles.practiceLayout}>
          <div>
            <p className={styles.sectionKicker}>Learning model</p>
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
            <p className={styles.sectionKicker}>Launch-ready learning</p>
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
      title="Build Public-Good Technology"
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
