import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const TrackList = [
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

const PracticeList = [
  'Read technical material like an engineer, not a passive student.',
  'Move from concept notes into reproducible labs and visible artifacts.',
  'Explain tradeoffs clearly across AI, blockchain, and distributed systems.',
  'Build toward open-source contribution instead of isolated coursework.',
];

function HeroSection() {
  return (
    <header className={styles.heroBanner}>
      <div className="container">
        <div className={styles.heroContent}>
          <p className={styles.heroEyebrow}>Flow Education Initiative</p>
          <Heading as="h1" className={styles.heroTitle}>
            Build public good technology in the open.
          </Heading>
          <p className={styles.heroSubtitle}>
            Structured tracks for developers contributing to AI/ML, blockchain,
            and protocol infrastructure. Rooted in African talent pipelines;
            open to builders everywhere.
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
              <dt>4</dt>
              <dd>tracks</dd>
            </div>
            <div>
              <dt>3</dt>
              <dd>skill levels</dd>
            </div>
          </dl>
        </div>
      </div>
    </header>
  );
}

function TracksSection() {
  return (
    <section className={styles.tracksSection}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <p className={styles.sectionKicker}>Curriculum</p>
          <Heading as="h2">A clear path from fundamentals to contribution</Heading>
          <p>
            The curriculum is organized around the capabilities engineers need
            to join serious open-source and infrastructure work.
          </p>
        </div>
        <div className={styles.trackGrid}>
          {TrackList.map((track) => (
            <article className={styles.trackCard} key={track.label}>
              <div className={styles.trackMeta}>{track.meta}</div>
              <p className={styles.trackLabel}>{track.label}</p>
              <h3>{track.title}</h3>
              <p>{track.detail}</p>
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
            <Heading as="h2">Built for engineers who learn by making things real</Heading>
            <p className={styles.practiceIntro}>
              Flow is not a content library for passive reading. Each track is
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
            <Heading as="h2">Start with the curriculum, then build in public.</Heading>
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
      description="Structured AI/ML, blockchain, and protocol engineering learning paths for contributors building practical public-good technology.">
      <HeroSection />
      <main>
        <TracksSection />
        <PracticeSection />
        <CtaSection />
      </main>
    </Layout>
  );
}
