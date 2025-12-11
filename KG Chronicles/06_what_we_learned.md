# What We Learned: A Knowledge Graph Playbook

## Looking Back

When our team started 17 sessions ago, knowledge graphs were an abstract concept. None of us were experts. We had questions about how they worked, whether we could actually build one, and what value they might deliver.

We set out to build something concrete: a working knowledge graph filled with product data, accessible through a conversational AI interface, working across multiple languages.

We succeeded. But more importantly, we learned something about the journey itself.

## What Went Well

### 1. Choosing the Right Domain

We selected electronics products—a domain none of us specialised in but all of us understood. This choice proved invaluable.

**Why it mattered**: You don't need to be a domain expert to build a knowledge graph. You need *accessible data*, *understandable relationships*, and *honest interest*. We had all three.

**Lesson**: Pick a domain where you can find data, understand the relationships, and stay motivated through challenges.

### 2. Designing Before Building

We spent significant time designing our ontology—the blueprint—before trying to load any data.

Yes, we adjusted it later. Yes, we learned more as we went. But having that initial structure meant we asked the right questions upfront:

- What entities do we need?
- What relationships matter?
- What are we actually trying to answer?

**Lesson**: Spend time on design, but don't let it paralyse you. Your design will evolve, and that's fine.

### 3. Iterating on Tools

We didn't stick with our first tool choice. We started with Protégé, learned what an ontology was, then moved to Neo4j when we needed to work with real data.

This wasn't a failure. It was necessary learning. Protégé taught us conceptual foundations. Neo4j taught us practical implementation.

**Lesson**: Choose tools pragmatically, not dogmatically. The best tool is the one that lets you move forward.

### 4. Treating Translation as a Structural Question

Instead of bolting translation on as an afterthought, we made it a core design decision. This affected our entire graph structure.

The result: translations aren't a second class of data. They're full relationships, linked like everything else. This made the graph more coherent and flexible.

**Lesson**: Consider multilingual needs early, even if you start with one language. It's far easier to design for it than to retrofit it.

### 5. Combining the Right Technologies

A knowledge graph alone is interesting but limited. An LLM alone is impressive but unreliable. Together, using RAG architecture, they create something genuinely useful.

This combination—reliable data plus conversational AI—unlocked use cases that neither could handle alone.

**Lesson**: Think about the complete system, not just individual components.

## What Was Hard

### Challenge 1: Data Is Messier Than You Think

Raw data is never clean. It has inconsistent naming, missing values, duplicate entries, and formats that don't match your expectations.

We spent more time cleaning data than building the graph structure. This isn't a failure—it's normal. It's also why automated approaches matter: using AI to analyse and clean data at scale saved us enormous time.

**What helped**: Building a data pipeline (extract, analyse, clean, load) rather than treating data cleaning as a one-time task.

### Challenge 2: Deciding What to Include

With 500+ properties available in our datasets, we had to decide: which ones matter?

Including everything creates clutter and slows queries. Including too little limits functionality. The balance came from asking: "What questions do we want to answer?" Properties that helped answer those questions stayed. Everything else went.

**What helped**: Creating a "question set" early—a list of questions users might ask. This became our North Star for deciding what to include.

### Challenge 3: Making the Graph Conversational

Translating natural language into graph queries isn't automatic. It requires:

- Understanding what the user is actually asking
- Translating that to graph semantics
- Handling edge cases (misspellings, variations in how people phrase things)

**What helped**: Starting with common question patterns and building out from there. We didn't try to handle every possible question; we got good at a core set and expanded systematically.

### Challenge 4: Balancing Simplicity and Richness

A graph can be beautifully simple or frustratingly limited. We constantly negotiated between:

- Simple enough that queries work reliably
- Rich enough that you can actually answer interesting questions

**What helped**: Starting minimal and adding complexity only when queries demanded it.

## Key Principles We'd Recommend

### Principle 1: Start With Questions, Not Data

Don't ask "What data do we have?" Ask "What questions do we want to answer?" Let those questions guide what data you collect and how you structure it.

Your ontology should reflect your questions, not the other way around.

### Principle 2: Design for Relationships, Not Just Properties

A knowledge graph's power comes from connections. When designing your structure, ask: "What relationships matter?" as often as "What properties do we need?"

In a traditional database, you might store "Samsung" as text in a phone record. In a graph, you create a relationship: this phone *is made by* Samsung. This single decision unlocks entire classes of queries.

### Principle 3: Iterate, Don't Perfectionise

Your first version won't be perfect. It will be wrong in interesting ways. That's not failure; it's data.

Load your data, run queries, see what breaks, fix it, repeat. This cycle teaches you far more than planning alone.

### Principle 4: Invest in Data Quality Early

Cleaning data is tedious and often overlooked. It's also the most important thing you can do. A graph with clean, consistent data is genuinely useful. A graph with messy data frustrates everyone.

Use automation (AI, scripts) to help, but prioritise this work.

### Principle 5: Make Multilingual a First-Class Feature

If you think you might ever need multiple languages, design for it from the start. Retrofitting translation is painful.

You don't need to translate everything—just identify what's language-dependent and what's universal.

### Principle 6: Combine Structured Data With Conversational AI

A knowledge graph is powerful, but it's not conversational by default. Connecting it to an AI system that can handle natural language makes it genuinely accessible.

This combination—reliable data plus intelligent interface—is becoming increasingly important.

## A Simple Roadmap

If you're considering building a knowledge graph, here's a path that worked for us:

### Phase 1: Learning and Design (Weeks 1-4)
- Define your domain and scope
- Create a question set: what will users ask?
- Design your ontology (structure)
- Choose your tools

### Phase 2: Data and Implementation (Weeks 5-10)
- Acquire your initial dataset
- Create a data pipeline (extract, clean, prepare)
- Build a small version of your graph
- Test queries against real questions

### Phase 3: Expansion and Integration (Weeks 11-16)
- Expand your graph with more data
- Handle special cases (translation, complex relationships)
- Connect to operational systems (websites, chatbots)
- Gather feedback and iterate

### Phase 4: Refinement and Operation (Ongoing)
- Monitor what works and what doesn't
- Add new languages, relationships, and data as needed
- Continuously improve query performance
- Maintain data quality

## What Becomes Possible

Once you have a working knowledge graph connected to an AI system, you can do things that were previously impossible:

**Accurate Conversational Search**
Users get results they trust because they're grounded in verified data.

**Relationship Discovery**
"What products are connected to this manufacturer?" becomes instant.

**Multilingual Access**
The same graph serves customers in any language you support.

**Reduced Hallucination**
Because the AI is retrieval-augmented, it's far less likely to make things up.

**Flexibility**
You can add new relationships and data types without redesigning everything.

**Domain-Specific Intelligence**
Unlike general-purpose AI, your system knows your data intimately and can answer specific questions accurately.

## The Bigger Picture

Knowledge graphs aren't new technology. What's new is that tools like Neo4j have made them accessible to small teams, and AI has made them conversational.

The organisations investing in knowledge graphs today aren't doing it for novelty. They're doing it because they have complex data they need to make sense of, in multiple languages, for global audiences, accessed by people who aren't data specialists.

This is increasingly common. It's why knowledge graphs are becoming mainstream.

## One More Thing: It's Worth the Effort

Building a knowledge graph requires thinking differently about data. It requires getting comfortable with design decisions that have no single "right" answer. It requires patience with messier-than-expected data.

But if you stick with it, you end up with something genuinely valuable: a single source of reliable information that can be queried, translated, explored, and made conversational.

Your data stops being a collection of isolated records and becomes a interconnected network of meaning.

And that changes everything.

---

## Resources to Explore

If you want to go deeper:

- **Neo4j Learning**: Official tutorials and documentation on property graphs and Cypher queries
- **Graph Data Science**: Once you have a graph, you can analyse it to find patterns and connections
- **RAG Systems**: Research papers and implementations on Retrieval Augmented Generation
- **Knowledge Graph Design**: Resources on ontology design and graph data modeling
- **Semantic Search**: Understanding vector embeddings and semantic similarity

## Final Thought

We built this knowledge graph not because we were experts, but because we had a problem to solve and the curiosity to figure it out. If you're considering a similar journey, know this: you don't need to be an expert to start.

You need to start to become an expert.

Good luck.

---

**The End — But Really, It's Just the Beginning**
