---
id: decentralized-identity
title: Decentralized Identity
track: blockchain
level: beginner
version: 1.1
---

# Decentralized Identity

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/8tS5c4KX7kU"
 title="Explaining Verifiable Credentials and Decentralized Identifiers"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Define decentralized identity (DID) and self-sovereign identity (SSI) in engineering terms.
- Explain the roles of DIDs, wallets, and verifiable credentials.
- Map decentralized identity concepts onto real-world systems (e.g., education, access control).
- Reason about how DIDs and credentials can be layered on top of L1/L2 blockchains.

## Concept Map

```mermaid
flowchart LR
 A["Issuer"] --> B["Credential"]
 B --> C["Holder"]
 C --> D["Verifier"]
 A --> E["DID document"]
 E --> D
```

## Quantitative Lens

Verification separates authenticity from authorization:

$$
Decision = verify(signature, issuerDID) \land check(policy, claim)
$$

## Introduction

Traditional identity systems are usually **centralized**: governments, corporations, or platforms issue and control your digital identity. In decentralized systems, the goal is different: identity should be **user-controlled, portable, and verifiable without a central authority**.

In the Flow Initiative, you will see **decentralized identity** as one way to:

- Represent users across protocols,
- Anchor trust to cryptographic proofs, and
- Reduce reliance on opaque, centralized identity providers.

This lesson treats decentralized identity as a **system design pattern**, not just "Web3 identity." You will learn the core primitives and how they can be composed with L1/L2 infrastructure.

## What Is Decentralized Identity?

Decentralized identity (often called **DID** or **SSI** - self-sovereign identity) is a model where:

- **Users own and control** their identifiers.
- **Credentials are issued once, stored by the user, and shared selectively**.
- **Verification is cryptographic** and can be done without contacting the issuer.

From an engineer's view, this is a **trust-minimized identity layer** that can sit on top of blockchains, distributed ledgers, or other public-goods infrastructure.

### Key Properties

- **User-controlled**: no single entity fully owns or revokes your identity.
- **Portable**: you can use the same identity across different services.
- **Privacy-preserving**: you can share only the attributes you choose.
- **Verifiable**: anyone can cryptographically verify that a claim is real.

These are not just philosophical goals; they are **design constraints** that shape how you build identity systems.

## Core Components

### 1. Decentralized Identifiers (DIDs)

A **DID** is a **persistent, user-controlled identifier** for a person, organization, or device.

- It looks like a string such as `did:example:123...`.
- It is **created by the user** (or via a wallet), not issued by a central registry.
- The DID **resolves to a DID Document** that contains public keys and service endpoints used to interact with the identity.

Crucially, the DID document typically **does not store private data**; it stores cryptographic material and endpoints that let others authenticate the identity.

### 2. Identity Wallets

An **identity wallet** is a software tool that:

- Stores the user's **private keys**.
- Manages multiple DIDs and associated credentials.
- Handles signing, encryption, and connection-establishment for DID-based protocols.

The wallet is the **user-facing layer** of the identity system, similar to how a blockchain wallet manages private keys for on-chain accounts.

### 3. Verifiable Credentials (VCs)

A **verifiable credential** is a cryptographically signed statement about the user, such as:

- "Issued by University X, this person completed Course Y."
- "Issued by Employer Z, this person is our employee."

Key properties:

- The **issuer signs** the credential with a private key.
- The **holder** stores it in their wallet.
- When needed, the holder can present a **proof** (often selective) to a **verifier**.

The verifier can check the signature against the issuer's public key (often stored on a DID) to confirm authenticity.

### 4. Trust Ecosystem

A **trust ecosystem** defines:

- Who is an allowed **issuer**.
- What **credential types** exist.
- How **revocation** or updates work.

This can be governed by a **decentralized trust framework** (e.g., a consortium-style governance body) rather than a single company or government.

## How DIDs and Credentials Work Together

A typical flow for decentralized identity looks like this:

1. **Setup**
 - The user creates a **DID** and stores it in a wallet.
 - The DID document is published to a blockchain or distributed ledger for discovery.

2. **Issuance**
 - An **issuer** (e.g., university, employer) creates a **verifiable credential** about the user.
 - The issuer signs the credential and sends it to the user's wallet.

3. **Storage**
 - The user keeps the credential in the wallet, possibly alongside others.
 - The user can choose which credentials to keep, delete, or rotate.

4. **Presentation**
 - A **verifier** (e.g., job platform, protocol, service) requests a proof of a specific attribute.
 - The wallet constructs a **cryptographic proof** (e.g., a zero-knowledge or selective-disclosure proof) and sends it.

5. **Verification**
 - The verifier checks:
 - The issuer's signature.
 - The credential's validity (e.g., not expired or revoked).
 - The verifier accepts or rejects the claim.

At no point is the user forced to share a full "profile." Only the required attributes are revealed.

## Why This Matters for Flow Engineers

Flow Initiative trainees will work on systems that need:

- **Cross-protocol identities** - the same person or node appearing in multiple chains and tools.
- **Trust-minimized verification** - confirming claims without calling a central authority for every check.
- **Privacy-respecting access control** - allowing users to share only what is necessary.

Decentralized identity helps you:

- Represent **students, engineers, or nodes** as reusable DIDs.
- Issue **certificates or achievements** as verifiable credentials.
- Design **access control** where the system checks proofs, not centralized databases.

In public-good contexts, this is especially relevant when:

- Centralized identity systems are fragmented or weak.
- Users want to control their data and move it across borders.
- Education and employment records need global, tamper-resistant verification.

## How Blockchain Fits In

Blockchain is not the only place to store decentralized identity data, but it is a natural fit for several pieces:

- **DID registries** - DID documents or DID roots can be anchored to a chain.
- **Credential registries** - hashes or revocation lists can be stored on-chain.
- **Governance** - on-chain protocols or L1s can coordinate issuers, verifiers, and rules for trust frameworks.

L1s and L2s can then:

- Accept **proofs** tied to DIDs,
- Verify credentials stored off-chain but referenced on-chain.

From an engineering standpoint, the chain is often the **issuance or verification anchor**, not the place where all user data lives.

## Practical Examples You Will Encounter

### Example 1: Education Credentials

- A university acts as an **issuer**.
- It issues **verifiable credentials** for degrees, transcripts, or course completions.
- Students store them in **identity wallets**.
- Employers act as **verifiers** and can instantly confirm authenticity without calling the registrar's office every time.

In Flow, this could become:

- A credential system for **completion of lessons or tracks**.
- A wallet-style interface for **trainees** where they collect Flow-issued credentials.

### Example 2: Node or Contributor Identity

- A decentralized protocol wants to identify **honest validators or contributors**.
- It issues **DIDs and credentials** to operators that pass certain tests.
- Those credentials can be reused across different services or layers.

Engineers can then design **stake-based or reputation-based** systems where credentials are part of the security model.

### Example 3: Cross-Platform Access

- A user has a DID issued by a trusted identity-provider network.
- Multiple services accept that DID as valid.
- The user never needs to create a new account on each service; they reuse their existing identity.

This is how you can reduce **authentication friction** while preserving control.

## Implementation Sketch

```json
{
 "id": "did:example:123",
 "verificationMethod": [{"id": "did:example:123#key-1", "type": "JsonWebKey2020"}]
}
```

## Practical Exercises

### Exercise 1: Sketch a Simple DID Flow

On paper or in a text editor, sketch a simple flow with three roles:

- **Holder** (user),
- **Issuer** (e.g., a "Flow Education" issuer),
- **Verifier** (e.g., a protocol or service).

For each step:

- Write what data or message is exchanged.
- Mark whether it is stored on-chain, in the wallet, or elsewhere.

This is a **mental model** of how the three roles interact.

### Exercise 2: Map a Real-World System to DIDs

Pick a real-world identity-heavy system you know (e.g., school ID, national ID, crypto wallet):

- Identify who currently acts as the **issuer** and who as the **holder**.
- Explain how DID-style identity would change that:
 - Who would now control the identifier?
 - Where would the credential live?
 - How would verification work?

Write a short note with your answers.

### Exercise 3: Relate to a Flow Lab

Imagine a Flow lab or future project that uses:

- User accounts,
- Reputation, or
- access control.

Design a small schema:

- Which entities should have DIDs?
- What kind of verifiable credentials should they hold?
- How would a verifier in that system check the credentials?

Write it in a markdown note so you can expand it later.

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what a DID and a verifiable credential are.
- I can see how DIDs differ from email-style identifiers.
- I can connect decentralized identity to real-world use cases (e.g., education, access control).
- I can imagine how DIDs and credentials might sit on top of an L1/L2 stack.

Action item: write a short note in your Flow lab repo describing one concrete place where DIDs and verifiable credentials could improve privacy or trust.

## Further Reading

- [W3C DID Core](https://www.w3.org/TR/did-core/)
- [W3C Verifiable Credentials](https://www.w3.org/TR/vc-data-model-2.0/)
- [DID use cases](https://www.w3.org/TR/did-use-cases/)
- [OpenID4VCI](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)

## Next Steps

- Read the next lesson in the `ecosystem` section (or the next track) that builds on identity and trust.
- Use this conceptual model whenever you encounter identity-focused protocols or specs.
- Treat decentralized identity as a **layered engineering primitive** that can be composed with L1/L2 systems, not as a separate "Web3 identity" silo.

---
