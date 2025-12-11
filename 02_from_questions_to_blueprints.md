# From Questions to Blueprints: Designing Your Knowledge Graph

## Choosing Where to Start

When you decide to build a knowledge graph, one of the first questions is: *What domain should we focus on?* This isn't a small decision. You're choosing the universe of information your graph will contain, and it shapes everything that comes next.

Our team considered three main options:

### Option 1: Medical Devices
Medical devices seemed perfect at first glance. They're highly regulated, require precise specifications, and would benefit enormously from clear relationships and structured data. The problem? None of us were medical experts. Building a graph in a domain you don't understand adds complexity you don't need when you're still learning.

**Lesson learned early**: Choose a domain you understand, or at least have access to people who do.

### Option 2: Regulated Industries (Finance, Law)
Similar reasoning. Yes, these industries would benefit from knowledge graphs. Yes, they'd use them well. But they're not fun to work with when you're learning, and we knew we'd need the motivation to push through challenges.

**The decision factor**: Pick a domain you'll actually enjoy exploring.

### Option 3: Electronics Devices
This was our choice, and for practical reasons:

1. **Data is accessible**: You can find product specifications online from retailers, manufacturer sites, and datasets like those on Kaggle. The data exists and is relatively public.

2. **Relationships are rich**: Electronics naturally have connections—computers have peripherals, phones have accessories, all devices connect to manufacturers and specifications. This gives a knowledge graph lots of interesting things to do.

3. **It's relatable**: Most people understand what a laptop is, what a phone does, and what features matter. We didn't need to become experts; we just needed to structure what we already knew.

4. **It has multiple layers**: We could store technical specifications, yes, but also user manuals, help articles, compatibility information, and eventually user reviews. This meant we weren't just managing dry data—we had room for richer content.

## Understanding Ontology: The Blueprint

Once we'd chosen our domain, the next step was to design what we called an "ontology." This word sounds complicated, but it's really just a blueprint—a plan for how your information will be organised.

Think of it this way: if a knowledge graph is a building, an ontology is the architectural drawing.

An ontology defines three main things:

### 1. Classes (or Types)
Classes are the categories of things you want to store. In our case, we decided on:

- **Electronic Device** (the broadest category)
  - Phone
  - Tablet
  - Computer
  - Smartwatch

Each class is more specific than the one above it. A Phone is a type of Electronic Device. This hierarchy matters because it means all Electronic Devices share certain properties (like a name and a manufacturer), while Phones have additional properties that only Phones need (like screen diagonal and cellular network type).

### 2. Properties
Properties are the characteristics of each class. For example, a Phone might have:

- Model name
- Screen size (in inches)
- Battery capacity (in mAh)
- Operating system
- Colour
- Weight
- Price

Not all properties apply to all classes. A Tablet doesn't need "cellular network type" in the same way. This flexibility matters.

### 3. Relationships
Relationships describe how classes connect to each other. For example:

- A Phone *is manufactured by* a Brand
- A Phone *has a* Colour
- A Phone *is sold by* a Retailer
- A Component *is part of* a Phone

This last point—relationships—is what makes knowledge graphs different from traditional databases. In a spreadsheet, you might have "Samsung" as data in a phone's row. In a knowledge graph, you create a connection: this phone *is linked to* Samsung. This distinction matters when you want to answer questions like "Show me all products from Samsung" or "What phones use this processor?"

## Building the Blueprint: Our First Ontology

Here's a simplified version of how we structured our initial ontology:

```
Electronic Device
├── Name: "Samsung Galaxy S25"
├── Manufacturer: [Link to Samsung Brand]
├── Model Number: "SM-S2500"
├── Description: "A flagship smartphone..."
├── Category: "Phone"
└── Properties:
    ├── Screen Size: 6.2"
    ├── Battery: 5000mAh
    ├── Processor: [Link to Processor Component]
    └── Colour: [Link to Colour]
```

When represented as connections (which is how knowledge graphs actually work internally), this becomes a series of relationships:

| What | Connected By | To |
|-----|-------------|---|
| Samsung Galaxy S25 | has manufacturer | Samsung |
| Samsung Galaxy S25 | has screen size | 6.2 inches |
| Samsung Galaxy S25 | has battery capacity | 5000mAh |
| Samsung Galaxy S25 | has colour | Midnight Black |

This might look simple, but it's powerful. Notice how we didn't just write "Samsung" as text. We created a *link* to Samsung. This means later, when we ask "What products are made by Samsung?", the graph can instantly find all devices linked to that brand.

## Why This Structure Matters

When you start designing an ontology, you make decisions that ripple through everything that comes next. Two decisions proved particularly important:

### Decision 1: What Should Be a Class vs. a Property?

Early on, we debated: should "Processor" be a class (with its own properties like brand, model, cores, speed), or just a property (text like "Intel i7")?

If it's a class, you can link multiple devices to the same processor, compare processors, and answer questions like "What's the difference between these two phones in terms of processor?"

If it's just a property, it's simpler to store but less flexible.

We eventually decided that shared things—processors, colours, manufacturers, batteries—should be classes, even if we didn't have complete data on them yet. This added a bit of complexity upfront but gave us flexibility later.

### Decision 2: Keep It Simple or Build for the Future?

We could have included dozens of properties for each device: exact dimensions, weight to the milligram, every connectivity standard, every sensor. We chose to start with the 20-30 properties that actually matter to someone choosing a device. We knew we could add more later.

This proved wise. It's easier to add properties than to redesign your ontology when you've already loaded thousands of records.

## Tools for Building Your Ontology

Before you can load data into a knowledge graph, you need to define this blueprint. We explored tools to help us:

**Protégé** (open-source, free) was our starting point. It's designed specifically for building ontologies and works well for learning. It lets you define classes, properties, and relationships visually. The downside? It's not very intuitive at first, and it's designed more for the semantic web standard (RDF) than for practical property graphs.

We documented our ontology in Protégé initially, then later moved to something more practical for our actual implementation.

## From Blueprint to Reality

Designing the ontology was perhaps the most important step we took. It forced us to think clearly about:

- What questions do we want to answer?
- What data do we have?
- How does that data connect?

Without this clarity, the next steps (finding data, loading it, querying it) would have been much harder.

In the next article, we'll see what happened when we actually tried to put real data into this structure. Spoiler: it was messier than we expected.

---

**Next: The Hard Part** — where we'll explore the reality of working with real data and choosing the right tools.
