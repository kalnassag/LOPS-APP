# The Hard Part: Data, Tools, and Real-World Decisions

## Reality Meets Planning

In theory, building a knowledge graph sounds straightforward: define your structure, find your data, load it, ask questions. In practice, the "find your data" part is where most projects encounter their first serious challenge.

## Finding and Sourcing Data

Our team looked at three options for getting product data:

### Option 1: Free, Publicly Available Datasets
Websites like Kaggle offer pre-packaged datasets. They're free, they're ready to use, and they're a great starting point. The problem? They're often incomplete, outdated, or inconsistent.

### Option 2: Commercial Data Services
Companies like TechSpecs maintain comprehensive, accurate databases of product information. The quality is excellent. The cost? Often thousands per year, which doesn't fit a learning project's budget.

### Option 3: Data Scraping
You write code to automatically pull information from websites. It's free, it's current, and it's often the most legally murky. For educational projects, it's reasonable—but it requires technical expertise and careful consideration of websites' terms of service.

We went with a hybrid approach: we used existing datasets to learn, and later considered scraping for more comprehensive data when the time was right.

## When Your Data Isn't Quite Right

Once you have data, you discover something humbling: it's almost never in the exact format you need.

Our first dataset included product specifications, but they had problems:

**Inconsistent property names**: One product's file might list "screen_size" while another uses "display_diagonal_inches". Same data, different names. Your graph needs consistency or it can't find things.

**Missing values everywhere**: A phone had a battery capacity listed, but a tablet didn't—not because tablets don't have batteries, but because the data was incomplete. You need to decide: do you ignore the missing data, mark it as unknown, or restructure your ontology?

**Duplicate properties with different formats**: A weight might be listed as "198g", "198 grams", "0.44 lbs", or not at all. Your graph can't query "find phones under 200 grams" if the data is stored in three different formats.

**Too many properties**: We had datasets with 500+ properties per product. Some were useful (screen size, battery, processor). Most were obscure technical specs we'd never actually query.

This is where you learn a crucial lesson: **data cleaning takes longer than loading data**. Our team spent weeks deciding which properties to keep, standardizing names, handling missing values, and removing duplicates.

## The Tools Question: Finding What Works

With our blueprint designed and data partially cleaned, we needed a tool to actually build and query our graph. This is where we encountered a key decision.

### Protégé: The Learning Tool

Remember Protégé, the ontology design tool from earlier? We started there because it's open-source and well-respected. The problem became clear quickly: Protégé is designed for a specific, academic standard called RDF (Resource Description Framework), which is powerful but complex. More practically, Protégé doesn't easily import CSV files or large datasets. Adding thousands of products meant clicking through menus repeatedly—not scalable.

Protégé is genuinely useful for *learning* what an ontology is and designing your structure. For actually *building* a working graph that you'll query and maintain, it falls short.

### Neo4j: The Practical Choice

Neo4j is a "graph database"—software specifically designed to store and query information as connections. Unlike Protégé, which is research-focused, Neo4j is built for real-world applications.

The key advantages for our project:

**1. It imports data easily**
You can upload CSV files, JSON, and other formats, then tell Neo4j how to map columns to your graph structure. This took hours instead of weeks.

**2. It has a practical query language**
Neo4j uses something called Cypher, which reads almost like English. For example:

```cypher
MATCH (phone:Phone) 
WHERE phone.price < 1000
RETURN phone.name, phone.brand
```

This finds all phones under $1,000 and returns their name and brand. It's intuitive.

**3. It's designed for exploration**
You can load data, see visualizations of your graph, test queries, and discover patterns. This exploratory capability is invaluable when you're learning.

**4. It works with AI**
Because Neo4j is built for modern applications, it integrates well with AI systems and chatbots—exactly what we needed for later phases of our project.

The choice to move to Neo4j was pragmatic, not academic. We weren't compromising on capability; we were choosing a tool built for our actual use case.

## A Brief Note on Graph Databases vs. Ontology Tools

You might wonder: are these the same thing? Not exactly, and understanding the difference is important.

**Ontology tools** like Protégé help you *design* your structure. They're focused on definitions, standards, and creating formally correct models. They're like an architect's drawing board.

**Graph databases** like Neo4j help you *implement* that structure with real data at scale. They're like the construction site itself.

In an ideal world, you might design your ontology in Protégé and then implement it in Neo4j. In practice, many teams skip Protégé and design their structure as they go with Neo4j, learning as they build.

For us, learning Protégé first taught us what an ontology *is*, which made using Neo4j much clearer. But if you're building practically, Neo4j (or similar tools) is where you'll actually live.

## Understanding Property Graphs

This is important: Neo4j doesn't work with the same model that Protégé's RDF uses. Neo4j uses something called a "property graph" model, and understanding this simplifies everything.

In a property graph, you have:

**Nodes**: Things. A phone, a brand, a colour. Each node can have properties (characteristics).

**Relationships**: Connections between nodes. "This phone *is made by* Samsung" or "This phone *has colour* Black".

**Properties on relationships**: Even connections can have data. "This phone *is sold in* Australia *at price* $999".

Here's a simple example:

```
Node: Samsung Galaxy S25
├── Type: Phone
├── Screen Size: 6.2"
├── Battery: 5000mAh
└── [is made by] ──→ Node: Samsung (Brand)
                      └── Country: South Korea

Node: Midnight Black
└── [has colour] ←── Samsung Galaxy S25
```

This model is intuitive because it matches how humans think about relationships. It's also practical because you can load real data quickly and query it without needing to understand complex academic standards.

## Decisions Made, Lessons Learned

Our choice to use Neo4j determined much of what came next:

- We could load our cleaned data relatively quickly
- We could visualize our graph and see if our design made sense
- We could write practical queries to answer business questions
- We had a foundation for integrating with AI systems

But first, we had to deal with one more reality: **the data was still messier than expected, and we had to make hard choices about what to include.**

In the next article, we'll explore those decisions, and then move into the more interesting territory: making the graph work across multiple languages.

---

**Next: Many Languages, One Graph** — where we tackle the challenge of building a multilingual knowledge graph.
