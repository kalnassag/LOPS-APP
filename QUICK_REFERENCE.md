# Knowledge Graph Quick Reference: Key Concepts & Visuals

## The Journey at a Glance

```
Phase 1: Understand & Design       Phase 2: Build & Implement       Phase 3: Enhance & Deploy
(Weeks 1-4)                        (Weeks 5-12)                      (Weeks 13+)

Domain Selection ──→ Ontology Design ──→ Data Sourcing ──→ Graph Building ──→ Translation Support
     ↓                    ↓                    ↓                ↓                    ↓
Electronics         Classes & Properties  Product specs    Load data       Multi-language setup
Products            Relationships          Clean & prepare  Query & test    AI Integration
                    Blueprint                               Visualise       Refinement
```

---

## Core Concepts

### 1. What Is a Knowledge Graph?

A knowledge graph is information stored as **connections** instead of isolated records.

**Traditional Database**:
```
Phone Record
├─ name: "Samsung Galaxy S25"
├─ manufacturer: "Samsung"
├─ price: "$899"
└─ color: "Midnight Black"
```

**Knowledge Graph**:
```
"Samsung Galaxy S25" 
├─[manufactured by]──→ "Samsung"
├─[costs]──→ "$899"
├─[colored]──→ "Midnight Black"
└─[similar to]──→ "Galaxy A25"
```

**Key difference**: The connections are as important as the data.

### 2. The Three Building Blocks

```
┌─────────────────────────────────────────────────────────┐
│                   KNOWLEDGE GRAPH                        │
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │    NODES     │  │ PROPERTIES   │  │ RELATIONSHIPS│  │
│  │              │  │              │  │              │  │
│  │ The things   │  │ Details about│  │ How things   │  │
│  │ themselves   │  │ those things │  │ connect      │  │
│  │              │  │              │  │              │  │
│  │ • Products   │  │ • Name       │  │ • Made by    │  │
│  │ • Brands     │  │ • Price      │  │ • Costs      │  │
│  │ • Colors     │  │ • Weight     │  │ • Similar to │  │
│  │ • People     │  │ • Specs      │  │ • Compatible│  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### 3. Ontology: The Blueprint

An ontology defines:
- **What types of things** you'll store (Classes)
- **What details** each thing has (Properties)  
- **How things relate** to each other (Relationships)

Example:

```
Class: Phone
├── Properties:
│   ├── name
│   ├── model_number
│   ├── screen_size
│   ├── battery_capacity
│   └── price
│
└── Relationships:
    ├── manufactured_by → Brand
    ├── has_colour → Colour
    ├── compatible_with → Accessory
    └── competitor_of → Phone
```

### 4. The Graph Query Language (Cypher)

How you ask questions to a knowledge graph.

**Simple query**: "Find all phones"
```cypher
MATCH (p:Phone)
RETURN p
```

**Filter query**: "Find phones under $500"
```cypher
MATCH (p:Phone)
WHERE p.price < 500
RETURN p.name, p.price
```

**Relationship query**: "Find all products made by Samsung"
```cypher
MATCH (p:Phone)-[:manufactured_by]->(b:Brand)
WHERE b.name = "Samsung"
RETURN p.name
```

**Translation note**: You're essentially saying:
"Find nodes of type Phone that have a relationship TO Brand nodes where the brand name is Samsung, then give me the phone names."

### 5. Three Approaches to Translation

```
┌────────────────────────────────────────────────────────────┐
│                 TRANSLATION APPROACHES                     │
├────────────────────────────────────────────────────────────┤
│                                                             │
│ Approach 1: Separate Copies                               │
│ ─────────────────────────────────────────────────────────  │
│ Graph_EN → Graph_DE → Graph_ES → Graph_FR                 │
│                                                             │
│ ✓ Simple                                                    │
│ ✗ Duplicates everything                                    │
│ ✗ Hard to keep in sync                                     │
│                                                             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│ Approach 2: Properties with Language Tags                 │
│ ─────────────────────────────────────────────────────────  │
│ Node: Samsung S25                                           │
│ ├── name_en: "Samsung Galaxy S25"                          │
│ ├── name_de: "Samsung Galaxy S25"                          │
│ ├── name_es: "Samsung Galaxy S25"                          │
│ └── name_fr: "Galaxy S25 de Samsung"                       │
│                                                             │
│ ✓ One graph                                                │
│ ✓ Clear which translations belong where                    │
│ ✗ Properties explode (50 properties × 6 languages)         │
│                                                             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│ Approach 3: Relationships to Translations (Our Choice)    │
│ ─────────────────────────────────────────────────────────  │
│ Samsung S25 (EN)                                            │
│ ├── [has_german_version] → Samsung S25 (DE)               │
│ ├── [has_spanish_version] → Samsung S25 (ES)              │
│ └── [has_color] → Midnight Black (shared across languages)│
│                                                             │
│ ✓ One graph                                                │
│ ✓ Scalable (add new language without changing structure)   │
│ ✓ Can share translations (color translated once)           │
│ ✗ Slightly more complex queries                            │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

### 6. RAG: How AI Meets Your Graph

RAG = Retrieval Augmented Generation

```
User Question: "Show me phones under $500"
        ↓
    [Natural Language Processor]
    (What does the user want?)
        ↓
    [Query Translator]
    (Convert to graph query)
        ↓
    [Knowledge Graph]
    (Execute query, find results)
        ↓
    [Results: Galaxy A25, Pixel 8a, iPhone 15]
        ↓
    [AI Language Model]
    (Generate natural response)
        ↓
Response: "Here are three great phones under $500..."
```

**Why this works**: 
- The graph provides accurate facts
- The AI provides conversational presentation
- Together: accurate AND natural

**Without the graph**: AI might make up phone specs  
**Without the AI**: Graph would require users to write queries

---

## Key Decision Points

### Decision 1: Domain Selection

```
? What problem are you solving?
? What data do you have access to?
? Do you understand the field?
? Will you stay interested?

✓ Our choice: Electronics products
  • Data was accessible
  • Domain was understandable
  • Relationships were clear
  • We could get real datasets
```

### Decision 2: What to Include

```
Too Minimal          Goldilocks Zone        Too Comprehensive
├─ 5 properties      ├─ 20-30 properties   ├─ 500+ properties
├─ Boring queries    ├─ Useful queries     ├─ Slow queries
├─ Easy to manage    ├─ Meaningful results ├─ Hard to maintain
└─ Limited usefulness└─ Balanced scope     └─ Analysis paralysis
```

### Decision 3: Node vs. Property

```
Should "Color" be a Property or Node?

Property:
Product.color = "Midnight Black"
├─ Simpler query
└─ But: "Midnight Black" stored separately for each product
   (duplicate text, hard to update across all products)

Node:
Product -[has_color]-> Color
├─ Slightly more complex query
├─ But: "Midnight Black" stored once
├─ Color can have translations in multiple languages
└─ Can find all products with this color instantly

Our choice: Node
(Shared things like colors and brands became nodes)
```

---

## Common Questions & Answers

### Q: Is this just a database with extra steps?

**A**: No. Databases are optimized for storing records. Knowledge graphs are optimized for understanding relationships. 

A database excels at: "Get me record #12345"  
A knowledge graph excels at: "What's related to this thing?" and "What connects A and B?"

### Q: Isn't this overly complicated?

**A**: It's complex only if you treat complexity as bad. The complexity handles real-world messiness:
- Multiple relationships between same entities
- Flexible structure that evolves
- Multilingual support built-in
- Natural language interfaces

The alternative is often more complex hidden systems.

### Q: How long does it take?

**A**: Our project took ~4 months (17 weeks) to go from nothing to working multilingual chatbot.

Breakdown:
- Weeks 1-4: Learning and design
- Weeks 5-10: Data and implementation  
- Weeks 11-16: Integration and refinement
- Ongoing: Maintenance and improvement

Your timeline depends on data complexity and team size.

### Q: Do we need a data science team?

**A**: No. You need:
- Someone who understands your domain
- Someone comfortable with data (analysis, cleaning)
- Someone technical (loading data, running queries)
- Someone focused on the outcome (business value)

These don't need to be separate people.

### Q: What if we get the ontology wrong?

**A**: You will get it wrong. And that's fine.

Load data, run queries, see what breaks, adjust. This is normal.

Your first ontology is never perfect. It's a starting point. The real learning comes from iteration.

---

## Tools Mentioned in the Series

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Protégé | Ontology design & visualization | Learning phase, small projects |
| Neo4j | Graph database & queries | Implementation, production |
| Cypher | Query language | All Neo4j queries |
| OpenRefine | Data transformation | Converting JSON to CSV, data cleaning |
| Python | Data scripts | Loading, transformation, automation |
| AI/LLM | Natural language interface | Making graph conversational |

---

## Success Metrics We Used

**Did the graph work if...**

- ✓ We could query it and get accurate results
- ✓ Data was consistent across the graph
- ✓ Queries returned results in under 100ms
- ✓ Translations were complete for key entities
- ✓ AI could understand and execute most user questions
- ✓ System worked across languages seamlessly

**What we didn't worry about:**

- Database size records (1500 nodes isn't huge, and that's fine)
- Complete dataset coverage (having 80% of data, well-structured, beats 100% of data, messy)
- Every possible query (focus on the important ones)
- Perfect translations (good translations matter more than complete translations)

---

## The Bigger Picture

```
Traditional Data Approach
├─ Data lives in silos (spreadsheets, databases, systems)
├─ Each team maintains their own copy
├─ Connections are implicit (you remember them)
├─ Adding new data types requires restructuring
└─ Non-technical people can't explore data independently

Knowledge Graph Approach
├─ Data unified in one place
├─ Single source of truth
├─ Connections are explicit (the graph knows them)
├─ New data types integrate naturally
└─ Natural language interface for everyone
```

---

## Resources for Next Steps

1. **Deeper Learning**: Neo4j free courses and certification
2. **Hands-On**: Build a small prototype on Neo4j (free tier available)
3. **Community**: Neo4j community forums and Stack Overflow
4. **Research**: Papers on RAG systems and semantic search
5. **Practice**: Identify your own domain and sketch an ontology

---

## Final Checklist: Are You Ready to Build?

- [ ] Do you have a clear problem or use case?
- [ ] Can you access relevant data?
- [ ] Can you identify 10-15 key questions users might ask?
- [ ] Do you have someone on the team comfortable with data?
- [ ] Do you have 8-16 weeks and team commitment?
- [ ] Can you start small and iterate?

If you checked 4+ boxes, you're ready.

Start small. Think relationships. Iterate often. Success will follow.

---

**End of Quick Reference**

For detailed explanations, return to the main article series.
