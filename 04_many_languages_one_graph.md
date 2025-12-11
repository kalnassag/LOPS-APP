# Many Languages, One Graph: Building for Global Audiences

## Why Language Matters

So far, everything in our knowledge graph was in English. But our team had a vision: what if the same graph could serve customers in Arabic, Chinese, German, Spanish, French, and Russian?

This isn't just about translating text. When you're building a product database for global audiences, language becomes a structural question. How do you store translations? How do you make sure searches work in any language? How do you update translations without breaking relationships?

These questions led us to explore several different approaches, each with trade-offs worth understanding.

## Three Approaches to Translation

### Approach 1: Separate Copies (The Easy but Costly Way)

The simplest solution: create a completely separate graph for each language.

```
Graph (English):
├── Samsung Galaxy S25
├── Screen: 6.2 inches
└── Colour: Midnight Black

Graph (German):
├── Samsung Galaxy S25
├── Bildschirm: 6,2 Zoll
└── Farbe: Mitternachtschwarz

Graph (Spanish):
├── Samsung Galaxy S25
├── Pantalla: 6,2 pulgadas
└── Color: Negro Medianoche
```

**Advantages**: Simple to implement. Each language works independently.

**Disadvantages**: You're duplicating your entire graph multiple times. Every update has to happen in every language. Relationships between languages (knowing that "Galaxy S25" and "Samsung Galaxy S25" are the same thing) become complex. Storage costs multiply.

We ruled this out quickly.

### Approach 2: Properties-Based Translation (Storing Text Variations)

The next idea: store all translations as properties on the same node.

```
Node: Samsung Galaxy S25
├── name_en: "Samsung Galaxy S25"
├── name_de: "Samsung Galaxy S25"
├── name_es: "Samsung Galaxy S25"
├── name_fr: "Galaxy S25 de Samsung"
├── screen_size: "6.2"
├── colour_en: "Midnight Black"
├── colour_de: "Mitternachtsschwarz"
├── colour_es: "Negro Medianoche"
└── colour_fr: "Noir Minuit"
```

**Advantages**: Single graph, no duplication. You know all translations belong to the same product because they're on the same node.

**Disadvantages**: Properties explode. Instead of one "name" field, you need six. If you have 50 properties and 6 languages, you're suddenly managing 300 property fields. It becomes hard to work with, and common properties like "colour" get duplicated across many products.

## Approach 3: Translation as Relationships (The Approach We Chose)

The insight came from thinking about language differently. Instead of storing translations *in* the node, create *relationships* to translated versions.

```
Node: Samsung Galaxy S25 (English)
├── name: "Samsung Galaxy S25"
├── [has_german_translation] ──→ Node: Samsung Galaxy S25 (German)
│                                  ├── name: "Samsung Galaxy S25"
│                                  └── [has_colour] ──→ "Mitternachtsschwarz"
│
├── [has_spanish_translation] ──→ Node: Samsung Galaxy S25 (Spanish)
│                                  ├── name: "Samsung Galaxy S25"
│                                  └── [has_colour] ──→ "Negro Medianoche"
│
└── [has_colour] ──→ Node: Midnight Black (English)
                     ├── name: "Midnight Black"
                     └── [has_german_translation] ──→ "Mitternachtsschwarz"
```

This approach treats translations as *connections*, just like other relationships in your graph.

**Advantages**: 
- Single graph, no duplication of core structure
- Each language version has only the properties needed for that language
- Shared things like colours can be translated once and linked to multiple products
- Searches in each language work naturally
- You can mix languages in queries if needed

**Disadvantages**: 
- Slightly more complex to query (you need to navigate translation relationships)
- Requires deliberate thinking about what needs translation vs. what's shared

## Making the Decision

We chose Approach 3, but getting there involved discovering something important: different types of data need different strategies.

### Unique Characteristics (Properties That Shouldn't Translate)

Some data is universal: a phone's screen size is 6.2 inches in any language. A battery capacity of 5000mAh doesn't change if you're shopping in English or French.

We stored these as regular properties: `screen_size: 6.2`, `battery_capacity: 5000`.

### Human-Readable Names (Properties That Should Translate)

Product names, descriptions, and specifications that humans read—these need translation.

Instead of duplicating properties, we created shared reference nodes for common things like colours and processors:

```
Node: Midnight Black
├── code: "color_001"
├── name_en: "Midnight Black"
├── name_de: "Mitternachtsschwarz"
├── name_es: "Negro Medianoche"
└── [applied_to_products] ──→ [All phones with this colour]
```

Now, any product that uses "Midnight Black" links to this single colour node. When you translate the colour once, it's translated for all products.

### Complex Content (Descriptions, Help Articles)

Later in our project, we imagined adding user manuals and help articles—longer text content. For this, we created locale-specific content nodes:

```
Node: Samsung Galaxy S25
├── [has_english_manual] ──→ Node: Manual_EN
│                             └── content: "Press and hold the power button to..."
│
├── [has_german_manual] ──→ Node: Manual_DE
│                            └── content: "Halten Sie die Einschalttaste..."
│
└── [has_spanish_manual] ──→ Node: Manual_ES
                              └── content: "Mantenga presionado el botón de encendido..."
```

This way, long content doesn't clog up the main product node, and translations are clearly linked.

## The Workflow: How It Actually Works

When you design a multilingual graph, you need a workflow:

**Step 1: Export and Identify**
Programmatically extract all text that needs translation from your graph. Tag what's translatable and what's not.

**Step 2: Translate**
Use translation services (human, AI, or both) to create translations. Store the mapping.

**Step 3: Load Back In**
Use a script to load translations back into the graph, creating the relationship structure we designed.

This means translation becomes a *process*, not a one-time task. Your graph is a living thing that gets updated.

## A Practical Example: Querying in Multiple Languages

Here's where the design really pays off. With our relationship-based approach, a simple query can work across languages:

```cypher
// Find all phones in English
MATCH (p:Phone)
RETURN p.name

// Find the German version of the same phones
MATCH (p:Phone)-[:has_german_translation]->(p_de:Phone)
RETURN p_de.name

// Find all products with a specific colour, regardless of language
MATCH (p:Phone)-[:has_colour]->(c:Colour)
WHERE c.code = "color_001"
RETURN p.name, c.name  // This will use the appropriate language
```

## Building for Expansion

One advantage of our approach: adding a new language doesn't require redesigning anything. You just create new translation nodes and relationships. If we wanted to add Portuguese tomorrow, we'd just:

1. Translate the necessary text
2. Create Portuguese nodes
3. Create relationships linking them

The core graph structure doesn't change.

## The Bigger Insight

What we learned is that translating a knowledge graph isn't just about finding the right words. It's about understanding what kind of data you have and making deliberate choices about how to store it.

Different data types need different strategies:
- **Universal data** (numbers, codes): Store once, use everywhere
- **Names and labels**: Create reference nodes that multiple products can link to
- **Long-form content**: Create locale-specific content nodes

This thinking forced us to be clearer about our data structure, which turned out to make everything—translation, maintenance, and querying—easier.

In the next article, we'll see what happens when you connect this multilingual graph to an AI system that can ask it questions in natural language.

---

**Next: The Conversation Begins** — where we'll explore how to make your knowledge graph answer questions like a chatbot.
