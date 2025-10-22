from neo4j import GraphDatabase

# URI = 'neo4j+s://e4f7116d.databases.neo4j.io'
# AUTH = ("neo4j", "ifHkrzNq3YpJkY9La9EWU71XhTzsyu_K4KAU_0ewmlI")

URI = "neo4j://127.0.0.1:7687"
AUTH = ("neo4j", "PythonLearn")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    try:
        driver.verify_connectivity()
        print("✅ Connection successful!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")

    with driver.session() as session:
        result = session.run("RETURN 'Hello Neo4j!' as message")
        record = result.single()
        print(record["message"])